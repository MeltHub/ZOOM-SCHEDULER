""" [ Import ] --------------------------------------------------------------------------------------------------- """

# Local에서 실행 시 pip으로 모듈을 설치해야 함.
# 현재 필요한 모듈 이외는 모두 주석 처리하였음.


# Import [ Qt UI ]
# from PyQt4.QtGui import

# Import [ Ftplib ]
# import ftplib

# Import [ OS ]
# import os

# Import [ URL Request ]
import urllib.request




""" [ 메인 ] --------------------------------------------------------------------------------------------------- """

# FTP Server State Check [ URL Download ]

url = 'http://datajunseo.ipdisk.co.kr:8000/list/HDD1/Server/ZOSC/INF/CHECK_INF.txt'
res = urllib.request.urlopen(url)
data = res.read()

State = data.decode("utf-8")

if State == "NORMAL":
    {
        print("FTP ON")}

else:
    {
        print(exit)}