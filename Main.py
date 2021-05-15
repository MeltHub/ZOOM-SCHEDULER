""" [ Import ] --------------------------------------------------------------------------------------------------- """

# Local에서 실행 시 pip으로 모듈을 설치해야 함.
# 현재 필요한 모듈 이외는 모두 주석 처리하였습니다.
# ( 주석 처리된 모듈은 모두 사용 예정입니다. )



# Import [ Qt UI ]
# from PyQt5.QtGui import
# import pyautogui as pg

# Import [ Ftplib ]
# import ftplib

# Import [ OS ]
# import os

# Import [ URL Request ]
import urllib.request

# Import [ configparser_ini File ]
import configparser



""" [ Main ] --------------------------------------------------------------------------------------------------- """

# Function (def) Section


# USER Information Check

def User():
    

    while True:
        ID = input("학번을 입력하세요 : ")
        

        if int(ID[0:1]) >= 4:
            print("학번을 제대로 입력해 주세요.\n")
            continue
        
        elif int(ID[1:3]) >= 14:
            print("학번을 제대로 입력해 주세요.\n")
            continue

        elif int(ID[3:5]) >= 35:
            print("학번을 제대로 입력해 주세요.\n")
            continue

        else:
            config_User = configparser.ConfigParser()
            config_User['User'] = {}
            config_User['User']['Grade'] = ID[0:1]
            config_User['User']['Class'] = ID[1:3]
            config_User['User']['Number'] = ID[3:5]
            break




    Name = input("\n이름을 입력하세요 : ")
    print("학번 : ",ID)
    print("이름: ",Name)

    
    config_User['User']['Name'] = Name

    with open('Setting.ini', 'w', encoding='utf-8') as configfile:
        config_User.write(configfile)

    print("\n[ 설정되었습니다 ]")




# FTP Server State Check [ URL Download ]

def State():

    url = 'http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/INF/CHECK_INF.txt'

    res = urllib.request.urlopen(url)

    data = res.read()

    State = data.decode("utf-8")

    if State == "NORMAL":
        print("\nFTP ONLINE")

    else:
        print("\nFTP OFFLINE")
        print(exit)




# Subject Schedule ZOSC.ini Create

def ZOSC_ini():

    Sub1, Sub2, Sub3, Sub4, Sub5, Sub6, Sub7 = input("테스트용 시간표 입력 : ").split()

    config_Subject = configparser.ConfigParser()
    config_Subject['Subject'] = {}
    config_Subject['Subject']['Subject1'] = Sub1
    config_Subject['Subject']['Subject2'] = Sub2
    config_Subject['Subject']['Subject3'] = Sub3
    config_Subject['Subject']['Subject4'] = Sub4
    config_Subject['Subject']['Subject5'] = Sub5
    config_Subject['Subject']['Subject6'] = Sub6
    config_Subject['Subject']['Subject7'] = Sub7

    with open('ZOSC.ini', 'w', encoding='utf-8') as configfile:
        config_Subject.write(configfile)
    





# Main Runtime


User()

State()

ZOSC_ini()

print(exit)