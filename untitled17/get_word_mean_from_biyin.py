import re
import requests
import pandas as pda
from bs4 import BeautifulSoup
import xlwt

path = "D:\\job_data\\6.xls"

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

#获取网站源码，主要是用于提取单词意思
def get_one_page(url):
    try:
        html = requests.get(url)
        return html.text
    except Exception:
        print("获取网站源码出错，请检查....................")

#解析获取单词意思
def get_word_mean(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        word_mean = soup.find_all('div', class_="each_seg")
        return word_mean
    except  Exception:
        print("解析单词意思出错，请检查.......................")

#获取网站源码，主要用于提取词性
def get_part_of_speech(html):
    try:
        soup = BeautifulSoup(html,'lxml')
        word_cixing = soup.find_all('div', class_="pos_lin")
        return word_cixing
    except Exception:
        print("解析词性出错,请检查.......................")

# 获取网站源码主要用于提取单词的词组
def get_code_to_Phrase(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        phrase = soup.find_all('div', class_="idm_seg")
        return phrase
    except Exception:
        print("获取单词词组出错，请检查....................")

#从获取的网站源码中提取出想要的词组并将其写入txt文档中
def get_word_phrase(phrase,file):
    try:
        for i in range(len(phrase)):
            parttern = re.compile('<span class="ids">(.*?)</span>.*?<span class="bil">(.*?)</span>.*?<span class="val">(.*?)</span>')
            items = re.findall(parttern,str(phrase[i]))
            k=1
            for item in items:
                file.write(str(k)+". "+str(item[0])+"\n")
                file.write(str(item[1])+" "+str(item[2])+"\n")
                k+=1
        file.close()
    except Exception:
        print("获取单词词组出错,请检查..........................")

#从获取的网站源码中提取出单词的词性
def get_word_cixing(word_cixing):
    try:
        cixing=[]
        for i in range(len(word_cixing)):
            soup1 = BeautifulSoup(str(word_cixing[i]),'lxml')
            content1 = soup1.find_all('div',class_="pos")
            for i in range(len(content1)):
                cixing.append(content1[i].text)
        return cixing
    except Exception:
        print("获取单词词性出错,请检查....................")

#解析网页源码，从中提取出单词的意思和词性并写入到txt文档中
def parse_one_page(k,word,word_mean,word_cixing,file):
    try:
        for i in range(len(word_mean)):
            soup1 = BeautifulSoup(str(word_mean[i]),'lxml')
            content1 = soup1.find_all('div',class_="se_lis")
            # print(cixing[i])
            file.write(str(word_cixing[i])+"\n")
            for j in range(len(content1)):
                file.write(str(content1[j].text)+"\n")
                # print(content1[j].text)
        file.close()
    except Exception:
        footer.write(k,0,word)
        wrongword.save('error_word_b_g.xls')
        print("获取单词意思出错,请检查..........................")

def main():
    key_word = get_data_from_excel()
    for i in range(len(key_word)):
        try:
            print("***********************"+key_word[i]+"****************************")
            # 定义文件路径，先将获取的单词意思全部都存入txt文档中，这样存入的数据就是一个整体，以便后续将数据写入excel做准备
            file = open("G:\\word_mean_a_c\\"+str(key_word[i])+".txt", 'w', encoding="utf-8")
            file1 = open("G:\\word_phrase_a_c\\"+str(key_word[i])+".txt", 'w', encoding="utf-8")

            url = "https://cn.bing.com/dict/search?q="+str(key_word[i])+"&qs=n&form=Z9LH5&sp=-1&pq="+str(key_word[i])
            html = get_one_page(url)
            word_mean = get_word_mean(html)
            word_cixing = get_part_of_speech(html)
            phrase = get_code_to_Phrase(html)
            get_word_phrase(phrase,file1)


            cixing = get_word_cixing(word_cixing)
            parse_one_page(i,key_word[i],word_mean,cixing,file)

        except Exception:
            footer.write(i,0,key_word[i])
            wrongword.save('error_word.xls')
            print("处理异常，请检查.............................")

if __name__ == "__main__":
    main()