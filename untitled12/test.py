import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')

worksheet.write(0, 0, 'a_word') # 不带样式的写入
worksheet.write(0, 1, 'b_alphabet')
worksheet.write(0, 2, 'c_meaning')

workbook.save('formatting.xls') # 保存文件