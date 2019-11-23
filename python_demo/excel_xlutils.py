import xlrd
from xlutils.copy import copy
import csv

rd_book = xlrd.open_workbook("test.xlsx")
#使用copy方法将xlrd.Book对象拷贝为一个xlwt.workbook对象，可写入
wt_book = copy(rd_book)
#获取一个sheet对象（支持index和name
ws = wt_book.get_sheet("S1")
#修改工作表
age = [32,39,34,22]
for j in range(len(age)):
    ws.write(j+1,1,age[j])

#保存文件
wt_book.save("test_new.xlsx")

