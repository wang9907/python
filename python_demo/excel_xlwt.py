import xlwt

#创建一个新的工作簿
wb = xlwt.Workbook(encoding="utf-8")
#在其上创建一个新的工作表
ws = wb.add_sheet("S1",cell_overwrite_ok=True)

#按单元格方式添加数据
ws.write(0,0,'HELLO')
#整行整列的添加数据
title = ['NAME','AGE','SEX','ADDRESS']
for i in range(len(title)):
    ws.write(0,i,title[i])

name = ['tom','smite','suixin','malke']
for j in range(len(name)):
    ws.write(j+1,0,name[j])

#保存文件
wb.save("test.xlsx")