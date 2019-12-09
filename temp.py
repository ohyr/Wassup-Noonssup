from PIL import Image
import numpy as np
import cv2


# file_path = sys.argv[1]
file_path = './uploads/111.jpg'
source_image = file_path
target_image = 'input_img3.jpg'
image = Image.open(source_image)
resize_image = image.resize((32, 32))
resize_image.save(target_image, 'JPEG', quality=95)

w = 32
h = 32
X = []
img = cv2.imread('input_img3.jpg')
img = cv2.resize(img, None, fx=w/img.shape[0], fy=h/img.shape[1])
X.append(img/256)

X = np.array(X)

categories = ["Blackpink Jennie","Blackpink Jisoo","Blackpink Lisa","Blackpink Rose","ChungHa","Gfriend EunHa",
              "Gfriend SinBi","Gfriend SoWon","Gfriend UmJi","Gfriend YeLin","Gfriend YuJoo","GongSeungYeon","HanGoEun",
              "JeonDoYeon","JeongChaeYeon","JinSeYeon","JoBoa","JooGyeolGyeong","KimAhJoong","KimGoEun","KimJiWon","KimSeJung",
              "KimSoHye","KimTaeRi","KimYooJung","LeeBoYoung","LeeMiyeon","LeeYeonHee","LimNaYoung","Mamamoo HwaSa","Mamamoo HwiIn",
              "Mamamoo MoonByeol","Mamamoo Sola","MinHyoLin","SeoHyunjin","ShinSeKyung","SongYuna","SooAe","Yujin","Chaeyoung","Dahyoen",
              "ITZY 류진","ITZY 리아","ITZY 신유나","ITZY 황예지","Irene","Jeongyoen","Jessica","Joy","Mina","Momo", "Seohyeon",
              "Nayeon","Sana","Seulgi","Suyoung","Taeyoen","Tiffany","Wendy","Yeri","ZZeuwi","jihyo","강소라","걸스데이 민아","걸스데이 소진",
              "걸스데이 유라","걸스데이 혜리","고소영","고아라","고준희","고현정","구혜선","김남주","김사랑","김성령","김소현","김연아","김태희","김하늘","김현주",
              "김혜수","김희선","김희애","문근영","문채원","박보영","박신혜","설현","손예진","송지효","송혜교","수지","신민아","에이핑크 김남주","에이핑크 박초롱",
              "에이핑크 손나은","에이핑크 오하영","에이핑크 윤보미","에이핑크 정은지","이나영","이하늬","임윤아","전지현","최지우","하지원","한가인","한예슬","한지민",
              "한효주","황신혜", '이영애']

X_test = X
xhat_idx = np.random.choice(X_test.shape[0], 5)
xhat = X_test[xhat_idx]

from keras.models import load_model
model = load_model('./models/female_rotate_111.h5')

yhat = model.predict_classes(xhat)
print(type(yhat[0]))
print(yhat[0])

answer = categories[yhat[0]]
print(answer)