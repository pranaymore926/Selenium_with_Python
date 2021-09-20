import openpyxl


def getRowCount(fileName , sheetName):
    workbook = openpyxl.load_workbook(fileName)
    sheet = workbook.get_sheet_by_name(sheetName)
    return (sheet.max_row)

def getColumnCount(fileName , sheetName):
    workbook = openpyxl.load_workbook(fileName)
    sheet = workbook.get_sheet_by_name(sheetName)
    return (sheet.max_column)


def readData(fileName , sheetName, rownum, columnnum):
    workbook = openpyxl.load_workbook(fileName)
    sheet = workbook.get_sheet_by_name(sheetName)
    return sheet.cell(row=rownum, column=columnnum).value


def writeData(fileName , sheetName, rownum, columnnum, data):
    workbook = openpyxl.load_workbook(fileName)
    sheet = workbook.get_sheet_by_name(sheetName)
    sheet.cell(row=rownum, column=columnnum).value=data
    workbook.save(fileName)


