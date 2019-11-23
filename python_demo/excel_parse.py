import re
import xlrd

#打开已有工作蒲
wb = xlrd.open_workbook("F:\data\平台医生目录表更改2019.11.23.xlsx");
#获取所有的sheet名称
sheet_names = wb.sheet_names();
print(sheet_names);
# 获取sheet对象
#ws = wb.sheet_by_index(0);
ws = wb.sheet_by_name("心血管内科");
#获取sheet对象的属性：表名、总行数、总列数
print(ws.name,ws.nrows,ws.ncols);

#获取某一行或某一列数据，返回list
row_4 = ws.row_values(3);
column_5= ws.col_values(4);
Row_4 = ws.row(3); #此方法list中包含单元格类型
Column_5=ws.col(4); #此方法list包含单元格类型

#遍历每一行，每一列
for x in range(ws.nrows):
    city = ws.cell_value(x,0);
    hospital = ws.cell_value(x, 1);
    department = ws.cell_value(x, 2);
    doctor = ws.cell_value(x, 3);
    print(city,hospital,department,doctor);

