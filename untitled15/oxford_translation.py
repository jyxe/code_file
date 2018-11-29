import re
import requests
import pandas as pda
from bs4 import BeautifulSoup
import xlwt

path = "D:\\job_data\\4.xls"
#指定file以utf-8的格式打开
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('word',cell_overwrite_ok=True)

#重新定义Excel,用于存放处理异常的单词
wrongword = xlwt.Workbook(encoding="utf-8")
footer = wrongword.add_sheet('sheet',cell_overwrite_ok=True)

#读取excel表中的单词
def get_data_from_excel():
    word = []
    data = pda.read_excel(path)
    data = data.values.tolist()
    for i in range(len(data)):
        # print(data[i][0])
        word.append(data[i][0])
    return word

#读取刚刚写入内容的txt文档，作为参数传递给wirte_content_to_excel
def read_data_from_txt(path):
    file = open(path,'r',encoding="utf-8")
    word_mean = file.read()
    return word_mean

#读取词组数据，将数据作为参数传给wirte_content_to_excel
def read_phrase_from_txt(path):
    file = open(path, 'r', encoding="utf-8")
    word_phrase = file.read()
    return word_phrase

#获取网站源码，主要是用于提取单词意思
def get_one_page(url):
    try:
        html = requests.get(url)
        # print(html.text)
        soup = BeautifulSoup(html.text,'lxml')
        content = soup.find_all('div', class_="each_seg")
        return content
    except Exception:
        print("解析出错，请检查....................")

#获取网站源码，主要用于提取词性
def part_of_speech(url):
    try:
        html = requests.get(url)
        # print(html.text)
        soup = BeautifulSoup(html.text,'lxml')
        content = soup.find_all('div', class_="pos_lin")
        return content
    except Exception:
        print("解析出错,请检查.......................")

#获取网站源码主要用于提取单词的音标
def get_code_to_pronunciation(url):
    try:
        html = requests.get(url)
        # print(html.text)
        soup = BeautifulSoup(html.text,'lxml')
        content = soup.find_all('div', class_="hd_tf_lh")
        return content
    except Exception:
        print("解析出错，请检查....................")


# 获取网站源码主要用于提取单词的词组
def get_code_to_Phrase(url):
    try:
        html = requests.get(url)
        # print(html.text)
        soup = BeautifulSoup(html.text, 'lxml')
        content = soup.find_all('div', class_="idm_seg")
        return content
    except Exception:
        print("解析出错，请检查....................")

#从获取的网站源码中提取出想要的词组并将其写入txt文档中
def get_word_phrase(html,file):
    try:
        for i in range(len(html)):
            parttern = re.compile('<span class="ids">(.*?)</span>.*?<span class="bil">(.*?)</span>.*?<span class="val">(.*?)</span>')
            items = re.findall(parttern,str(html[i]))
            k=1
            for item in items:
                file.write(str(k)+". "+str(item[0])+"\n")
                file.write(str(item[1])+" "+str(item[2])+"\n")
                k+=1
        file.close()
    except Exception:
        print("获取单词词组出错,请检查..........................")

#从获取的网站源码中提取出单词的发音
def get_word_pronunciation(html):
    try:
        for i in range(len(html)):
            soup1 = BeautifulSoup(str(html[i]),'lxml')
            content1 = soup1.find_all('div',class_="hd_p1_1")
            if(len(content1[i].text)>5):
                return content1[i].text
            else:
                return ""
    except Exception:
        print("获取单词发音出错,请检查..........................")

#从获取的网站源码中提取出单词的词性
def get_part_of_speech(html):
    try:
        cixing=[]
        for i in range(len(html)):
            soup1 = BeautifulSoup(str(html[i]),'lxml')
            content1 = soup1.find_all('div',class_="pos")
            for i in range(len(content1)):
                cixing.append(content1[i].text)
        return cixing
    except Exception:
        print("获取单词词性出错,请检查....................")

#解析网页源码，从中提取出单词的意思和词性并写入到txt文档中
def parse_one_page(k,word,html,cixing,file):
    try:
        for i in range(len(html)):
            soup1 = BeautifulSoup(str(html[i]),'lxml')
            content1 = soup1.find_all('div',class_="se_lis")
            # print(cixing[i])
            file.write(str(cixing[i])+"\n")
            for j in range(len(content1)):
                file.write(str(content1[j].text)+"\n")
                # print(content1[j].text)
        file.close()
    except Exception:
        footer.write(k,0,word)
        wrongword.save('error_word_b_g.xls')
        print("获取单词意思出错,请检查..........................")

#将读取的数据存放到excel表格中
def wirte_content_to_excel(i,word,pronunciation,word_mean,word_phrase):
    for j in range(4):
        if (j==0):
            worksheet.write(i,j,word)
        if (j==1):
            worksheet.write(i,j,pronunciation)
        if (j==2):
            worksheet.write(i,j,word_mean)
        if (j==3):
            worksheet.write(i,j,word_phrase)

def main():
    key_word = get_data_from_excel()
    for i in range(len(key_word)):
        try:
            print("***********************"+key_word[i]+"****************************")
            # 定义文件路径，先将获取的单词意思全部都存入txt文档中，这样存入的数据就是一个整体，以便后续将数据写入excel做准备
            file = open("G:\\word_mean\\"+str(key_word[i])+".txt", 'w', encoding="utf-8")
            file1 = open("G:\\word_phrase\\"+str(key_word[i])+".txt", 'w', encoding="utf-8")
            path = ("G:\\word_mean\\"+str(key_word[i])+".txt")
            path1 = ("G:\\word_phrase\\"+str(key_word[i])+".txt")
            url = "https://cn.bing.com/dict/search?q="+str(key_word[i])+"&qs=n&form=Z9LH5&sp=-1&pq="+str(key_word[i])
            html3 = get_code_to_Phrase(url)
            get_word_phrase(html3,file1)
            html = get_one_page(url)
            html1 = part_of_speech(url)
            html2 = get_code_to_pronunciation(url)
            cixing = get_part_of_speech(html1)
            parse_one_page(i,key_word[i],html,cixing,file)
            pronunciation = get_word_pronunciation(html2)
            word_mean = read_data_from_txt(path)
            word_phrase = read_phrase_from_txt(path1)
            wirte_content_to_excel(i,key_word[i],pronunciation,word_mean,word_phrase)
            # print(word_phrase)
            # print(pronunciation)
            workbook.save("word_d_g.xls")
        except Exception:
            print("处理异常，请检查.............................")

if __name__ == "__main__":
    main()