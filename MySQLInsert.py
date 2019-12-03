# Stupid import from 1127 to 1202,What a shit!
import io
import datetime
import MySQLdb

# 打开本地文件
f = io.open("../Data/1202塔防数据统计.txt", "r", encoding="utf-8")

# 定义一个方法
def monsterData():
    db = MySQLdb.connect("localhost", "root", "mysql123", "Monster", charset='utf8')
    cursor = db.cursor()

    #用空格切割数据
    data = str(f.read()).split(' ')
    for i in range(len(data)):
        #每循环一次，记录时间增加一分钟
        timeMark = (datetime.datetime(2019, 10, 1, 00, 00, 00) + datetime.timedelta(minutes=i)).strftime("%H%M")
        #每循环一次，插入一条数据
        sqlInsert = "INSERT INTO December(monsterID,recordID,week,date)VALUES(%s,%s,%s,%s)"%(data[i], '"'+timeMark+'0'+data[i]+'"','1','20191202')

        try:
            cursor.execute(sqlInsert)
            db.commit()
            
        # 出错回滚
        except:
            db.rollback()
    #关闭数据库连接
    db.close()

# 时间初始格式模板
# n = (datetime.datetime(2019, 10, 1, 23, 59, 00)+datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

# 执行方法
monsterData()

# 注意：注释基本添加于GitHub，可能存在缩进问题。
