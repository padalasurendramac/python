import xlrd

workbook = xlrd.open_workbook("DataFile.xlsx")
sheet = workbook.sheet_by_name("login")

#get total number of rows:
rowCount = sheet.nrows
colCount = sheet.ncols
print(colCount)
print(rowCount)

for curr_row in range(1, rowCount):
    user_name = sheet.cell_value(curr_row, 0)
    password = sheet.cell_value(curr_row, 1)
    
    print(user_name + " " + password)