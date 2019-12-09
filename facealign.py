import sys
import dlib
import cv2
import align_dlib as openface
import os
import numpy as np


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8): 
    try: 
        n = np.fromfile(filename, dtype) 
        img = cv2.imdecode(n, flags) 
        return img 
    except Exception as e: 
        print(e) 
        return None

def imwrite(filename, img, params=None): 
    try: 
        ext = os.path.splitext(filename)[1] 
        result, n = cv2.imencode(ext, img, params) 
        if result: 
            with open(filename, mode='w+b') as f: 
                n.tofile(f) 
                return True 
        else: 
                return False 
    except Exception as e: 
        print(e) 
        return False
    


# Create a HOG face detector using the built-in dlib class
predictor_model = "shape_predictor_68_face_landmarks.dat"
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

# Take the image file name from the command line
file_name = sys.argv[1]
img_name = file_name.split('/')[1]
img_name_1 = img_name.split('.')[0]

#파일저장명
alignfile=os.path.split(file_name)
alignfile=alignfile[1]

#파일이름으로 폴더생성
file_path=os.path.splitext(file_name)
file_path=os.path.split(file_path[0])
folder_path=file_path[1]

# Load the image
image = imread(file_name)

#resize the img
resized_img = cv2.resize(image, (300, 400), interpolation=cv2.INTER_AREA)
imwrite('./uploads/' + img_name_1 + '_1.jpg', resized_img)

# Run the HOG face detector on the image data
detected_faces = face_detector(image, 1)

# Loop through each face we found in the image
for i, face_rect in enumerate(detected_faces):
    # Get the the face's pose
    pose_landmarks = face_pose_predictor(image, face_rect)
    # Use openface to calculate and perform the face alignment
    alignedFace = face_aligner.align(96, image, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    
    #uploads에 폴더 없으면 폴더 만들고 align 이미지 저장
    dir_path='uploads'
    if not os.path.exists(dir_path+folder_path):
        os.mkdir(dir_path+'/'+folder_path+'/')
    
    # Save the aligned image to a file
    imwrite(os.path.join(dir_path+'/'+folder_path+'/',alignfile),alignedFace)

    
    
