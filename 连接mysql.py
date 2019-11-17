import pymysql

# python建立与mysql连接
db = pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="study",charset="utf8")

# 建立游标
cursor = db.cursor()

# sql = """create table stu(
#     id int not null,
#     name varchar(8) not null,
#     age int
# )
# """
# cursor.execute(sql)

# sql = "insert into stu(id,name,age) values (2,'张琴',27)"  # 新增数据

# sql = "select * from stu"
# cursor.execute(sql)
# data = cursor.fetchall() # 获取查询到的所有数据
# data1 = cursor.fetchone()   获取单行数据
# print(data[1][1])              # 查询结果为元组


# sql = "update stu set name = '天华' where id = 1"
# cursor.execute(sql)
# db.commit()
# print("OK")

sql = "delete from stu where name ='天华'"
sql2 = "delete from stu where name ='张琴'"
try:
    cursor.execute(sql)
    cursor.execute(sql2)
    db.commit()
except Exception as e:
    db.rollback()       # 回滚
    print("出现异常!")
print("ok")
db.close()