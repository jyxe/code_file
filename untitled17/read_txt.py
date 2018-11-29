import pandas as pda
import requests
from bs4 import BeautifulSoup

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

for i in range (len(miss_mean)):
    print(miss_mean[i])
    url = "https://cn.bing.com/dict/search?q="+str(miss_mean[i])+"&qs=n&form=Z9LH5&sp=-1&pq="+str(miss_mean[i])
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    word_mean = soup.find_all('div', class_="li_pos")
    try:
        for j in range(len(word_mean)):
            print(word_mean[i])
    except:
        print("获取单词意思出错............")
    # url=""
    # html = requests.get()
# re_miss_word = []
# for j in range(len(miss_mean)):
#     try:
#         path1 = "G:\\word_miss_word2\\"+str(miss_mean[j])+".txt"
#         file2 = open(path1,'w',encoding='utf-8')
#
#         data3 = file2.read()
#         if (len(data3) == 0):
#             re_miss_word.append(miss_mean[j])
#     except Exception:
#         re_miss_word.append(miss_mean[j])
#         print("文件不存在")
# print(re_miss_word)
#
# # second_miss_word=[]
# #
# # for num in range(len(re_miss_word)):
# #     try:
# #         path5 = "G:\\word_miss_word1\\"+str(re_miss_word[num])+".txt"
# #         file5 = open(path5,'r',encoding='utf-8')
# #         data5 = file5.read()
# #         if(len(data5)==0):
# #             second_miss_word.append(re_miss_word[num])
# #     except Exception:
# #         print("没有文件夹")
# #
# # print(len(second_miss_word))
