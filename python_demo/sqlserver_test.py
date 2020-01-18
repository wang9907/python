import pymssql

conn=pymssql.connect(host='10.10.1.65',user='sa',password='pingce@204',database='gk',charset="GBK")
'''
如果和本机数据库交互，只需修改链接字符串
conn=pymssql.connect(host='.',database='Michael')
'''
cur=conn.cursor()

cur.execute('select top 5 * from [dbo].[CMN_USR_INF]')
#如果update/delete/insert记得要conn.commit()
#否则数据库事务无法提交
print (cur.fetchall())

cur.close()

conn.close()
