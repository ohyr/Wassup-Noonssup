import sys
import numpy as np
import cv2
from keras.models import load_model


def make_answer():
    file_path = sys.argv[1]
    gender = sys.argv[2]
    num = sys.argv[3]
    source_image = file_path
    img_name = file_path.split('/')[1]
    img_name_1 = img_name.split('.')[0]
    target_image = './uploads/' + img_name_1 + '/' + img_name

    w = 32
    h = 32
    X = []
    img = cv2.imread(target_image)
    img = cv2.resize(img, None, fx=w/img.shape[0], fy=h/img.shape[1])
    X.append(img/256)

    X = np.array(X)

    categories_female = ["Blackpink Jennie","Blackpink Jisoo","Blackpink Lisa","Blackpink Rose","ChungHa","Gfriend EunHa",
            "Gfriend SinBi","Gfriend SoWon","Gfriend UmJi","Gfriend YeLin","Gfriend YuJoo","GongSeungYeon","HanGoEun",
            "JeonDoYeon","JeongChaeYeon","JinSeYeon","JoBoa","JooGyeolGyeong","KimAhJoong","KimGoEun","KimJiWon","KimSeJung",
            "KimSoHye","KimTaeRi","KimYooJung","LeeBoYoung","LeeMiyeon","LeeYeonHee","LimNaYoung","Mamamoo HwaSa","Mamamoo HwiIn",
            "Mamamoo MoonByeol","Mamamoo Sola","MinHyoLin","SeoHyunjin","Seohyeon","ShinSeKyung","SongYuna","SooAe","Yujin","Chaeyoung","Dahyoen",
            "ITZY Ryujin","ITZY Lia","ITZY Yuna","ITZY Yeji","Irene","Jeongyoen","Jessica","Joy","Mina","Momo",
            "Nayeon","Sana","Seulgi","Suyoung","Taeyoen","Tiffany","Wendy","Yeri","ZZeuwi","jihyo","KangSora","Gday MinA","Gday SoJin",
            "Gday Yura","Gday Hyeri","KoSoyoung","KoAra","KoJunheui","KoHyunjeong","KooHyesun","KimNamju","KimSarang","KimSungryung","KimSohyun","KimYuna","KimTaeheui","KimHaneul","KimHyunju",
           "KimHyesu","KimHeuisun","KimHeuiae","MunGeunyoung","MunChaewon","ParkBoyoung","ParkShinhye","Seolhyun","SonYejin","SongJihyo","SongHyegyo","Suji","ShinMina","Apink Namju","Apink Chorong",
            "Apink Naeun","Apink Hayoung","Apink Bomi","Apink Eunji","LeeNayoung","LeeYoungae","LeeHaneui","LimYuna","JeonJihyun","ChoiJiwu","Hajiwon","HanGain","HanYeseul","HanJimin",
           "HanHyoju","HwangShinhye"]

    categories_male = ['Btob LimHyunSik', 'Btob Pniel', 'Btob SeoEunGwang', 'Chanmin', 'Choisiwon', 
           'Day6 DoWoon','Day6 YoungK', 'EXO KAI', 'EXO Dio', 'EXO Ray', 'EXO Baekhyun',
           'EXO Sehun', 'EXO Suho', 'EXO Chanyeol', 'EXO Chen', 'Eunhyuk', 'Gangin', 'Gyuhyun',
           'Heuicheol', 'Hoya', 'HyunBin', 'Jhope', 'Jimin', 'Jungguk', 'KangDongWon',
           'KimSooHyun', 'Kimsunggyu', 'KoSoo', 'L', 'Leekikwang', 'Namwoohyun',
           'Nuest Ren', 'ParkYucheon', 'RM', 'Ryuwook', 'Seventeen DoGyeom', 
           'Seventeen JeongHan', 'Seventeen Scoups', 'Shindong', 'Sondongwoon',
           'SongJoongGi', 'SongSeungHeon', 'Sugar', 'TOP', 'V', 'Yesung', 'Yongjunhyeong', 'YooSeungHo',
           'Yunho','Day6 SungJin','Day6 WonPil','JangDongGun','JoInSung','JeongWooSung','Btob LeeMinHyuk',
            'Btob YookSungJae','ChaEunWoo','Nuest Aron','Nuest BaekHo','Seventeen MinGyu','WonBin',
            'Gseven jb', 'Gseven Jackson', 'Gseven Jinyoung', 'KangHaneul', 'Gongyu',
           'KwonSangwu', 'KimMinjong', 'KimWubin', 'RyuJunyeol','ParkBogeom', 'ParkHaejin', 'SoJisub',
           'SongIlguk', 'Wone KangDaniel', 'Wone Raigwanlin', 'Wone ParkWujin',
           'Wone ParkJihun', 'Wone BaeJinyoung', 'Wone OngSeongwu',
           'Wone HaSungwun', 'Wone HwangMinhyun', 'Winner KangSeungyun', 'Winner KimJinwu',
           'Winner SongMinho', 'Winner LeeSeunghun', 'YuAin', 'LeeMinho', 'LeeByungheon', 'LeeSeojin',
           'LeeSeungki', 'LeeJeongjae', 'LeeJongseok', 'JangGeunseok', 'Janghyuk', 'JeongHaein', 'ChoSeungwu',
           'JiChangwuk', 'ChaSeungwon', 'ChaInpyo', 'ChoiMinsu', 'ChoiSujong', 'Pio', 'HaJeongwu']

    X_test = X
    xhat_idx = np.random.choice(X_test.shape[0], 5)
    xhat = X_test[xhat_idx]

    male_model_path = ''
    female_model_path = ''

    if num == '1':
        male_model_path = './models/male_rotate_104.h5'
        female_model_path = './models/female_rotate_111.h5'
    elif num == '2':
        male_model_path = './models/male_rotate_change1.h5'
        female_model_path = './models/female_rotate_change1.h5'
    elif num == '3':
        male_model_path = './models/male_rotate_model_3.h5'
        female_model_path = './models/female_rotate_model_3.h5'


    if gender == 'female':
        model = load_model(female_model_path)
    else:
        model = load_model(male_model_path)

    yhat = model.predict_classes(xhat)

    if gender == 'female':
        answer = categories_female[yhat[0]]
    else:
        answer = categories_male[yhat[0]]

    print(answer)
    sys.stdout.flush()

make_answer()
