#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']

total = []
row_id = 1;
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		total.append(ws.cell(row = row_id, column = 7).value)
	row_id += 1

#grade구하기

total.sort(key=lambda x:x[1], reverse=True)
num = len(total)

for i in range (num):
        ws.cell(row = total[i][0], column = 8).value = 'C0'
for i in range(int (num * 0.85)):
        ws.cell(row = total[i][0], column = 8).value = 'C+'
for i in range(int (num * 0.7)):
        ws.cell(row = total[i][0], column = 8).value = 'B0'
for i in range(int (num * 0.5)):
        ws.cell(row = total[i][0], column = 8).value = 'B+'
for i in range(int (num * 0.3)):
        ws.cell(row = total[i][0], column = 8).value = 'A0'
for i in range(int (num * 0.15)):
        ws.cell(row = total[i][0], column = 8).value = 'A+'

wb.save("student.xlsx")
