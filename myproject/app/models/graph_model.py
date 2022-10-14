import pymysql
import sqlite3

# conn = sqlite3.connect("sensor_data_test")   # 저장할 DB파일 이름
# curs = conn.cursor()
# curs.execute("SELECT * FROM ID")

# data = curs.fetchall

# conn.commit()  #커밋 (쌓아둔 명령 실행)
# conn.close()


# mysql
# class Database():
#     def __init__(self): # 생성자
#         self.db = pymysql.connect(host='localhost',
#                                   user='root',
#                                   password='',
#                                   db='',
#                                   charset='utf8')
#         self.cursor = self.db.cursor()

#     def execute(self, query, args=[]):
#         self.cursor.execute(query, args)

#     def executeOne(self, query, args=[]):
#         self.cursor.execute(query, args)
#         row = self.cursor.fetchone()
#         return row

#     def executeAll(self, query, args=[]):
#         self.cursor.execute(query, args)
#         rows = self.cursor.fetchall()
#         return rows

#     def executeMany(self, query, n):
#         self.cursor.execute(query)
#         rows = self.cursor.fetchmany(n)
#         return rows

    # def commit():
    #     self.db.commit() # database가 정의되어있지않아서 ???


# sqlite3
class Database():
    def __init__(self): # 생성자
        self.conn = sqlite3.connect("sensor_data.db")
        self.curs = self.conn.cursor()

    def execute(self, query, args=[]):
        self.curs.execute(query, args)
        
    def executeOne(self, query, args=[]):
        self.curs.execute(query, args)
        row = self.curs.fetchone()
        return row

    def executeAll(self, query, args=[]):
        self.curs.execute(query, args)
        rows = self.curs.fetchall()
        return rows

    def executeMany(self, query, n):
        self.curs.execute(query)
        rows = self.curs.fetchmany(n)
        return rows

    # def commit():
    #     self.conn.commit()
    #     self.conn.close()