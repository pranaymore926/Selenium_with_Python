import openpyxl
path = 'C:\\Users\prana\Downloads\WriteData.xlsx'

workbook = openpyxl.load_workbook(path)
sheet = workbook.active


for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r , column=c).value = "Welcome to Tabahistan"

#you must save data else test will run and nothing will be written in excel
workbook.save(path)