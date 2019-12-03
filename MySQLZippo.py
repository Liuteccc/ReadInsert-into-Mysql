# encoding=utf-8

from collections import Counter
import operator
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "mysql123", "Monster", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 选中所有数据
sqlSelect = "Select recordID FROM November WHERE monsterID IN (3,4,5,6)"

try:
	# 执行sql语句
	cursor.execute(sqlSelect)
	# 返回结果
	results = cursor.fetchall()

except:
	# 发生错误时回滚
	db.rollback()

# 关闭数据库连接
db.close()


# 统计出现频率，并倒序排列
matchNum = dict(Counter(results))
matchResults = sorted(matchNum.items(), key=operator.itemgetter(1), reverse=True)
print(matchResults[0:100])








