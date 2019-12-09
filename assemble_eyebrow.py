import cv2
import numpy as np
import dlib
import sys

# 얼굴 검출기와 랜드마크 검출기 생성 --- ①
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

# 얼굴 및 랜드마크 검출해서 좌표 반환하는 함수 ---②
def getPoints(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects = detector(gray)
    points = []
    for rect in rects:
        shape = predictor(gray, rect)
        a = (shape.part(17).y - shape.part(19).y)
        b = (shape.part(22).x - shape.part(21).x)
        a = int(a)
        b = int(0)
        part = shape.part(17)
        points.append((part.x - b, part.y))
        part = shape.part(26)
        points.append((part.x + b, part.y))
        for i in range(17, 26):
            part = shape.part(i)
            points.append((part.x, part.y))
        part = shape.part(27)
        points.append((part.x, part.y))

    return points

# 랜드마크 좌표로 들로네 삼각형 반환 ---③
def getTriangles(img, points):
    w, h = img2.shape[:2]
    subdiv = cv2.Subdiv2D((0, 0, w, h));
    subdiv.insert(points)
    triangleList = subdiv.getTriangleList();
    triangles = []
    for t in triangleList:
        pt = t.reshape(-1, 2)
        if not (pt < 0).sum() and not (pt[:, 0] > w).sum() \
                and not (pt[:, 1] > h).sum():
            indice = []
            for i in range(0, 3):
                for j in range(0, len(points)):
                    if (abs(pt[i][0] - points[j][0]) < 1.0 \
                            and abs(pt[i][1] - points[j][1]) < 1.0):
                        indice.append(j)
            if len(indice) == 3:
                triangles.append(indice)
    return triangles


# 삼각형 어핀 변환 함수 ---④
def warpTriangle(img1, img2, pts1, pts2):
    x1, y1, w1, h1 = cv2.boundingRect(np.float32([pts1]))
    x2, y2, w2, h2 = cv2.boundingRect(np.float32([pts2]))

    roi1 = img1[y1:y1 + h1, x1:x1 + w1]
    roi2 = img2[y2:y2 + h2, x2:x2 + w2]

    offset1 = np.zeros((3, 2), dtype=np.float32)
    offset2 = np.zeros((3, 2), dtype=np.float32)
    for i in range(3):
        offset1[i][0], offset1[i][1] = pts1[i][0] - x1, pts1[i][1] - y1
        offset2[i][0], offset2[i][1] = pts2[i][0] - x2, pts2[i][1] - y2

    mtrx = cv2.getAffineTransform(offset1, offset2)
    warped = cv2.warpAffine(roi1, mtrx, (w2, h2), None, \
                            cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)

    mask = np.zeros((h2, w2), dtype=np.uint8)
    cv2.fillConvexPoly(mask, np.int32(offset2), (255))

    warped_masked = cv2.bitwise_and(warped, warped, mask=mask)
    roi2_masked = cv2.bitwise_and(roi2, roi2, mask=cv2.bitwise_not(mask))
    roi2_masked = roi2_masked + warped_masked
    img2[y2:y2 + h2, x2:x2 + w2] = roi2_masked


if __name__ == '__main__':
    # 이미지 읽기 ---⑤
    contour_img = sys.argv[1]
    destination_img = sys.argv[2]
    num = sys.argv[3]    

    # 경로 파싱
    img_name = destination_img.split('/')[1]
    folder_name = img_name.split('.')[0]    

    # eyebrow contour
    img1 = cv2.imread(contour_img)

    # destination img
    img2 = cv2.imread(destination_img)
    img_draw = img2.copy()

    # 각 이미지에서 얼굴 랜드마크 좌표 구하기--- ⑥
    points1 = getPoints(img1)
    points2 = getPoints(img2)

    # 랜드마크 좌표로 볼록 선체 구하기 --- ⑦
    hullIndex = cv2.convexHull(np.array(points2), returnPoints=False)
    hull1 = [points1[int(idx)] for idx in hullIndex]
    hull2 = [points2[int(idx)] for idx in hullIndex]

    # 볼록 선체 안 들로네 삼각형 좌표 구하기 ---⑧
    triangles = getTriangles(img2, hull2)

    # 각 삼각형 좌표로 삼각형 어핀 변환 ---⑨
    for i in range(0, len(triangles)):
        t1 = [hull1[triangles[i][j]] for j in range(3)]
        t2 = [hull2[triangles[i][j]] for j in range(3)]
        warpTriangle(img1, img_draw, t1, t2)

    # 볼록선체를 마스크로 써서 얼굴 합성 ---⑩
    mask = np.zeros(img2.shape, dtype=img2.dtype)
    cv2.fillConvexPoly(mask, np.int32(hull2), (255, 255, 255))
    r = cv2.boundingRect(np.float32([hull2]))
    center = ((r[0] + int(r[2] / 2), r[1] + int(r[3] / 2)))
    output = cv2.seamlessClone(np.uint8(img_draw), img2, mask, center, \
                               cv2.NORMAL_CLONE)

    # 합성 사진 저장
    cv2.imwrite('./uploads/' + folder_name + '/' + folder_name + '_eyebrow' + num + '.jpg', output)
