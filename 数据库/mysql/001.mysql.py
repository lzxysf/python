import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  port='3306',
  user='lzxysf',
  passwd='216857'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS project_db')
mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)

print(mydb)


# 我们可以直接连接数据库，如果数据库不存在，会输出错误信息
mydb = mysql.connector.connect(
  host='localhost',
  port='3306',
  user='lzxysf',
  passwd='216857',
  database='project_db'
)
mycursor = mydb.cursor()

mycursor.execute("drop table if exists users")
mycursor.execute("create table if not exists users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age VARCHAR(255))")
mycursor.execute("alter table users add column sex VARCHAR(255)")

mycursor.execute("show tables")
for x in mycursor:
    print(x)

sql = "insert into users(name,age,sex) values(%s,%s,%s)"
val = ('liming', '23', 'man')
mycursor.execute(sql, val)
mydb.commit()             # 数据表内容有更新必须使用commit

# 批量插入
# 批量插入使用executemany()方法，该方法第二个参数是一个元组列表，包含了要插入的数据
val = [
  ('lina', '34', 'woman'),
  ('wangming', '23', 'man'),
  ('liyang', '12', 'man'),
  ('denny', '21', 'man'),
  ('jenny', '17', 'woman')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount)    # 插入数据条数
print(mycursor.lastrowid)   # 最后一个插入命令插入行的第一行的主键，这个表必须是有自动增长的id，否则获取到的值为0

# 查询数据 fetchall
mycursor.execute("select * from users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# 查询一条数据 fetchone
myresult = mycursor.fetchone()
print(myresult)
