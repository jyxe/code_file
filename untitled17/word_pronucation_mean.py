import pandas as pda
import requests
from bs4 import BeautifulSoup
import xlwt
path = "D:\\job_data\\word.xlsx"


#指定file以utf-8的格式打开
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('word',cell_overwrite_ok=True)

data = pda.read_excel(path)
data1 = data.values.tolist()

for i in range(len(data1)):
    try:
        print("*******************************"+str(data1[i])+"************************************")
        path1 = "G:\\word_pronucation\\"+data1[i][0]+".txt"
        path2 = "G:\\word_mean_a_z\\" + data1[i][0] + ".txt"

        file1 = open(path1,'r',encoding="utf-8")
        file2 = open(path2, 'r', encoding="utf-8")

        data2 = file1.read()
        data3 = file2.read()

        for j in range(3):
            if (j == 0):
                worksheet.write(i, j, data1[i])
            if (j == 1):
                worksheet.write(i, j, data2)
            if (j == 2):
                worksheet.write(i, j, data3)

    except Exception:
            worksheet.write(i,0,data1[i])
            print("文件读取异常")
workbook.save("word1.xls")
