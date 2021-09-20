#install openpyxl
#pip install openpyxl
#Read data from excel file
#Write data to excel
#import data to test script
import openpyxl

path = 'C:\\Users\prana\Downloads\LoginData.xlsx'

workbook = openpyxl.load_workbook(path)
sheet = workbook.active     #workbook.get_sheet_by_name

rows = sheet.max_row
cols = sheet.max_column

print(rows)
print(cols)

for r in range(1, rows+1):
    for c in range(1, cols+1):
        print(sheet.cell(row=r , column=c).value)
