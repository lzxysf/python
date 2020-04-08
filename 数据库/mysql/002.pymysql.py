import pymysql

mydb = pymysql.connect('localhost', 'lzxysf', '216857', 'project_db')
mycursor = mydb.cursor()
mycursor.execute('select version()')
myresult = mycursor.fetchone()
print(myresult)

sql = "drop table if exists employees"
mycursor.execute(sql)
mydb.commit()

sql = """create table employees(
        first_name varchar(20) not null,
        last_name varchar(20),
        age int,
        sex varchar(1),
        income float)"""
try:
        mycursor.execute(sql)
        mydb.commit()
except Exception:
        mydb.rollback()    # 发生错误时回滚

sql = """insert into employees(first_name,
         last_name, age, sex, income)
         values ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
        mycursor.execute(sql)
        mydb.commit()
except Exception:
        mydb.rollback()
        print('执行错误')


# 查询
# fetchone() 该方法获取下一个查询结果集 
# fetchall() 接收全部的返回结果行
# rowcount 这是一个只读属性，并返回执行excute()方法后影响的行数
# 查询不改变数据表的内容，所以不需要调用db.commit

sql = 'select * from employees where income >= 2000'
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        print('{},{},{},{}'.format(fname, lname, age, sex))

mydb.close()
