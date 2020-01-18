import re
import xlrd

#打开已有工作蒲
wb = xlrd.open_workbook("D:\新建文件夹\国康系统\\23专家管理\\02专家导入功能\平台医生目录表更改2019.11.23.xlsx");
#获取所有的sheet名称
sheet_names = wb.sheet_names();
print(sheet_names);
# 获取sheet对象
#ws = wb.sheet_by_index(0);
ws = wb.sheet_by_name("心血管内科");
#获取sheet对象的属性：表名、总行数、总列数
#print(ws.name,ws.nrows,ws.ncols);

#获取某一行或某一列数据，返回list
row_4 = ws.row_values(3);
column_5= ws.col_values(4);
Row_4 = ws.row(3); #此方法list中包含单元格类型
Column_5=ws.col(4); #此方法list包含单元格类型

#从文件读取各种数据集
citys = open("D:\新建文件夹\国康系统\\23专家管理\\02专家导入功能\城市.txt","r",encoding="utf-8").readlines();
#去掉读取处理换行符
for i in range(len(citys)):
    citys[i] = citys[i].strip();
deps = open("D:\新建文件夹\国康系统\\23专家管理\\02专家导入功能\科室.txt","r",encoding="utf-8").readlines()
for i in range(len(deps)):
    deps[i] = deps[i].strip();
hosps = open("D:\新建文件夹\国康系统\\23专家管理\\02专家导入功能\医院.txt","r",encoding="utf-8").readlines()
for i in range(len(hosps)):
    hosps[i] = hosps[i].strip();
#print(deps)
#print('深圳' not in citys)
#遍历每一行，每一列
for x in range(ws.nrows):
    str = "";
    city = ws.cell_value(x,0);
    if city not in citys:
       str += city+","
    hospital = ws.cell_value(x, 1);
    if hospital not in hosps:
       str += hospital+","
    department = ws.cell_value(x, 2);
    if department not in deps:
       str += department+","
    doctor = ws.cell_value(x, 3);
    if(str != ''):
        print(str);

