# Stupid import from 1127 to 1202,What a shit!
import io
import datetime
import MySQLdb

f = io.open("../Data/1202塔防数据统计.txt", "r", encoding="utf-8")

def monsterData():
    db = MySQLdb.connect("localhost", "root", "mysql123", "Monster", charset='utf8')
    cursor = db.cursor()

    data = str(f.read()).split(' ')
    for i in range(len(data)):
        timeMark = (datetime.datetime(2019, 10, 1, 00, 00, 00) + datetime.timedelta(minutes=i)).strftime("%H%M")
        sqlInsert = "INSERT INTO December(monsterID,recordID,week,date)VALUES(%s,%s,%s,%s)"%(data[i], '"'+timeMark+'0'+data[i]+'"','1','20191202')

        try:
            cursor.execute(sqlInsert)
            db.commit()
        except:
            db.rollback()
    db.close()

# 时间初始格式模板
# n = (datetime.datetime(2019, 10, 1, 23, 59, 00)+datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

monsterData()
