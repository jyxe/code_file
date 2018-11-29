import pandas as pda
import requests
from bs4 import BeautifulSoup

path = "D:\\job_data\\6.xls"


data = pda.read_excel(path)
data1 = data.values.tolist()
# print(data1)
miss_pronucation = []
for i in range(len(data1)):
    try:
        # print("*******************************"+str(data1[i])+"************************************")
        path1 = "G:\\word_pronucation\\"+data1[i][0]+".txt"
        file = open(path1,'r',encoding="utf-8")
        data2 = file.read()
        if (len(data2)==0):
            miss_pronucation.append(data1[i][0])
            print(data1[i])
    except Exception:
        miss_pronucation.append(data1[i][0])
        print("文件不能存在")

print(miss_pronucation)