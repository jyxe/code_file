import re
import requests
import pandas as pda
from bs4 import BeautifulSoup
import xlwt

path = "D:\\job_data\\word.xlsx"
#读取excel中的单词
def read_word_from_excel():
    data = pda.read_excel(path)
    data1 = data.values.tolist()
    # print(data1)
    miss_mean = []
    for i in range(len(data1)):
        try:
            print("*******************************" + str(data1[i]) + "************************************")
            path1 = "G:\\word_mean_a_z\\" + data1[i][0] + ".txt"
            file = open(path1, 'r', encoding="utf-8")
            data2 = file.read()
            if (len(data2) == 0):
                miss_mean.append(data1[i][0])
        except Exception:
            # print("文件夹不存在")
            # print("*********************************")
            miss_mean.append(data1[i][0])
    return miss_mean

#获取网站源码
def get_one_page(url):
    try:
        html = requests.get(url)
        return html.text
    except Exception:
        print("解析出错，请检查....................")

#提取包含意思的代码
def get_word_mean_html(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        word_mean_html = soup.find_all('div', class_="each_seg")
        return word_mean_html
    except Exception:
        print("获取单词意思出错.................")

#提取包含词性的代码
def part_of_speech(html):
    try:
        soup = BeautifulSoup(html,'lxml')
        cixing_html = soup.find_all('div', class_="pos_lin")
        return cixing_html
    except Exception:
        print("解析单词词性出错,请检查.......................")

#从获取的网站源码中提取出单词的词性
def get_part_of_speech(cixing_html):
    try:
        cixing=[]
        for i in range(len(cixing_html)):
            soup1 = BeautifulSoup(str(cixing_html[i]),'lxml')
            content1 = soup1.find_all('div',class_="pos")
            for i in range(len(content1)):
                cixing.append(content1[i].text)
        return cixing
    except Exception:
        print("获取单词词性出错,请检查....................")

#解析网页源码，从中提取出单词的意思和词性并写入到txt文档中
def parse_one_page(word_mean_html,cixing,file):
    try:
        for i in range(len(word_mean_html)):
            soup1 = BeautifulSoup(str(word_mean_html[i]),'lxml')
            content1 = soup1.find_all('div',class_="se_lis")
            # print(cixing[i])
            file.write(str(cixing[i])+"\n")
            for j in range(len(content1)):
                file.write(str(content1[j].text)+"\n")
                # print(content1[j].text)
        file.close()
    except Exception:
        print("获取单词意思出错,请检查..........................")


def main():
    key_word = read_word_from_excel()
    for i in range(len(key_word)):
        try:
            print("***********************"+key_word[i]+"****************************")
            # 定义文件路径，先将获取的单词意思全部都存入txt文档中，这样存入的数据就是一个整体，以便后续将数据写入excel做准备
            file = open("G:\\word_miss_word2\\"+str(key_word[i])+".txt", 'w', encoding="utf-8")

            url = "https://cn.bing.com/dict/search?q="+str(key_word[i])+"&qs=n&form=Z9LH5&sp=-1&pq="+str(key_word[i])
            html = get_one_page(url)
            word_mean_html = get_word_mean_html(html)
            cixing_html = part_of_speech(html)
            cixing = get_part_of_speech(cixing_html)
            parse_one_page(word_mean_html, cixing, file)
        except Exception:
            print("获取单词意思出错................")

if __name__ == "__main__":
    main()