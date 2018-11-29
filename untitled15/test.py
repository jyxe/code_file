import xlwt
import pandas as pda


workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('word',cell_overwrite_ok=True)

path = "D:\\job_data\\1.xlsx"
data = pda.read_excel(path)
data = data.values.tolist()
for i in range(len(data)):
    file = open("G:\\word_mean\\"+data[i][0]+".txt",'r',encoding="utf-8")
    mean = file.read()
    for j in range(2):
        if(j==0):
            worksheet.write(i,j,data[i][0])
        else:
            worksheet.write(i,j,mean)
        print(mean)

workbook.save("biying.xls")

# worksheet.write(i, k, key_word[i])