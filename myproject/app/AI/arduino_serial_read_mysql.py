#1. python -m pip install --upgrade pip
#2. 환경 변수 추가(Path) : python 설치 경로 + \Scripts
#   ex: C:\Users\owner\AppData\Local\Programs\Python\Python310\Scripts
#3. pip install pyserial

#import csv, sqlite3

import mysql.connector
import string
from turtle import st
import serial
import time
from datetime import datetime

now = datetime.now()
# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)

# DB 연결
mysql_con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1111",
    database="Smartfarm",
    port=3600
)

#커서 생성
mysql_cursor = mysql_con.cursor(dictionary=True)

# 1. CONNECT MYSQL : DB 테이블 생성은 while 바깥에서 한번만 하는게 좋습니당
mysql_cursor.execute("CREATE TABLE IF NOT EXISTS ID(no INTEGER AUTO_INCREMENT PRIMARY KEY,Datetime Datetime, M FLOAT, D FLOAT, H FLOAT,T FLOAT)")
# AUTO_INCREMENT는 데이터들 유니크하게 사용할 수 있도록 아이디로써 쓰기 위함. INSERT 시 값 채우지 않아도 알아서 카운팅 됨. (+ Primary Key)
print("Create Table")


while True:
    data = ser.readline()

    # 데이터에는 개행문자 \r\n이 들어가므로, 해당 개행문자가 없을 경우 데이터가 아니므로 넘어가기.
    bytes = data
    result = bytes.decode('utf-8')
    result1 = result.strip()
    
    if len(result1) == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
         continue 
    #if result.rfind('\r\n') == -1:
    #   continues
    strings = result1.split('_')
    strings1 = list(map(float, strings))
    strings2 = list(map(int, strings1))      

    # b'{data}_{data}...\r\n' 형태이므로 b''부분 자르기 SADSAADAWDWAWA
    data1 = strings2[:len(data) - 4]

    print(data1)
    to_db = [(strings2[0]), (strings2[1]),(strings2[2]),(strings2[3])]
    mysql_cursor.execute("INSERT INTO ID(M, D, H, T) VALUES(%s, %s,%s, %s);", to_db) #to_db 수정해야함
    mysql_cursor.execute("ALTER TABLE ID MODIFY Datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP;")

    mysql_con.commit()  #커밋 (쌓아둔 명령 실행)

mysql_con.close()
