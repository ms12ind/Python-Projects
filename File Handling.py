import openpyxl
from  openpyxl import Workbook
w=Workbook()
sheet=w.active
sheet['A1']="Hello"
w.save("mybook.xlsx")

wb=openpyxl.load_workbook("mybook.xlsx")
sheet=wb.active
c=sheet['A1'].value
print(c)