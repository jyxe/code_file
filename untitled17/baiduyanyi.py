import re
from bs4 import BeautifulSoup
import pandas as pda
import numpy as npy
import requests
import json
import urllib3
import xlwt

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('mean1',cell_overwrite_ok=True)

wrongword = xlwt.Workbook(encoding = 'utf-8')
wrong = workbook.add_sheet('mean2',cell_overwrite_ok=True)

urllib3.disable_warnings()

url = "https://fanyi.baidu.com/basetrans"
path = "D:\\job_data\\word.xlsx"
data = pda.read_excel(path)
data1 = data.values.tolist()
# print(data1)
miss_mean = []
for i in range(len(data1)):
    try:
        print("*******************************"+str(data1[i])+"************************************")
        path1 = "G:\\word_mean_a_z\\"+data1[i][0]+".txt"
        file = open(path1,'r',encoding="utf-8")
        data2 = file.read()
        if (len(data2)==0):
            miss_mean.append(data1[i][0])
    except Exception:
        # print("文件夹不存在")
        # print("*********************************")
        miss_mean.append(data1[i][0])

for k in range(len(miss_mean)):
    try:
        print("***************************"+miss_mean[k]+"*******************************")
        path2 = "G:\\word_pronucation2\\"+str(miss_mean[k])+".txt"
        file = open(path2,'w',encoding='utf-8')

        query_str = miss_mean[k]
        data = {
            "query": query_str,
            "from": "en",
            "to": "zh"}
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "Referer": "https://fanyi.baidu.com/?aldtype=16047&tpltype=sigma"
        }

        response = requests.post(url, data=data, headers=headers,verify=False)
        html_str = response.content.decode()  # json字符串

        # json数据交换格式，使用json之前需要导入
        # 把json字符串转化为Python类型
        dict_ret = json.loads(html_str)
        pronunciation = "美：["+dict_ret["dict"]["symbols"][0]["ph_am"]+"]  "+"英: ["+dict_ret["dict"]["symbols"][0]["ph_en"]+"]"
        file.write(pronunciation)
        file.close()

    except Exception:
        print("获取音标错误..............................")