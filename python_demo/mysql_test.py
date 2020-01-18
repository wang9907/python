import  pymysql

config = {
    "host":"10.10.1.38",
    "user":"hjc",
    "password":"hjc",
    "database":"dbtest"
}
#连接数据库
#db = pymysql.connect("10.10.1.38","hjc","hjc","dbtest")
db = pymysql.connect(**config)
#使用cursor()方法创建一个游标对象
cursor = db.cursor()
#使用excute()方法执行SQL语句
cursor.execute("select * from area limit 10")
#使用fetchall()获取全部数据
data = cursor.fetchall();
#打印获取到的数据
for x in data:
    print(x)


#关闭游标和数据库连接
cursor.close()
db.close()

