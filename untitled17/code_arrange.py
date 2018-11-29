import re
import pandas as pda
from bs4 import BeautifulSoup
import xlwt
import requests
import json
import urllib3

path = "D:\\job_data\\6.xls"
url1 = "https://fanyi.baidu.com/basetrans"
urllib3.disable_warnings()
#重新定义Excel，用户存放正确的单词
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('mean1',cell_overwrite_ok=True)

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

def get_word_pronucation(key_word):
    try:
        data = {
            "query": key_word,
            "from": "en",
            "to": "zh"}
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "Referer": "https://fanyi.baidu.com/?aldtype=16047&tpltype=sigma"
            }

        response = requests.post(url1, data=data, headers=headers, verify=False)
        html_str = response.content.decode()

        # 把json字符串转化为Python类型
        dict_ret = json.loads(html_str)
        pronunciation = "美：["+dict_ret["dict"]["symbols"][0]["ph_am"]+"]"+"英:["+dict_ret["dict"]["symbols"][0]["ph_en"]+"]"
        return pronunciation

    except Exception:
        print("获取单词音标出错.........................")

#从获取的网站源码中提取出想要的词组并拼接成字符串
def get_word_phrase(phrase):
    try:
        word_phrase = ""
        for i in range(len(phrase)):
            parttern = re.compile('<span class="ids">(.*?)</span>.*?<span class="bil">(.*?)</span>.*?<span class="val">(.*?)</span>')
            items = re.findall(parttern,str(phrase[i]))
            k=1
            for item in items:
                word_phrase="".join(str(k)+". "+item[0]+"\n"+item[1]+item[2])
                # word_phrase = " "+str(k)+". "+str(item[0])+"\n"+str(item[1])+" "+str(item[2])+"\n"
                k+=1
        return word_phrase
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

# 解析网页源码，从中提取出单词的意思词性和意思然后将其拼接成字符串
def get_word_meaning(k, word, word_mean, word_cixing):
    try:
        word_meaning = ""
        for i in range(len(word_mean)):
            soup1 = BeautifulSoup(str(word_mean[i]), 'lxml')
            content1 = soup1.find_all('div', class_="se_lis")
            word_meaning = ""+str(word_cixing[i])+"\n"
            for j in range(len(content1)):
                word_meaning = ""+str(content1[j].text)+"\n"

        return word_meaning

    except Exception:
            footer.write(k, 0, word)
            wrongword.save('error_word_b_g.xls')
            print("获取单词意思出错,请检查..........................")

#解析网页源码，从中提取出单词的所有信息并写入Excel
def parse_one_page(k,word,word_pronucation,word_mean,word_phrase):
    try:
        for j in range(4):
            if (j == 0):
                worksheet.write(k, j, word[k])
            if (j == 1):
                worksheet.write(k, j, word_pronucation)
            if (j == 2):
                worksheet.write(k, j, word_mean)
            if (j == 3):
                worksheet.write(k, j, word_phrase)
        workbook.save("word_oxford_a_z.xls")
    except Exception:
        footer.write(k,0,word)
        wrongword.save('error_word_b_g.xls')
        print("获取单词意思出错,请检查..........................")

def main():
    key_word = get_data_from_excel()
    for i in range(len(key_word)):
        try:
            print("***********************"+key_word[i]+"****************************")

            url = "https://cn.bing.com/dict/search?q="+str(key_word[i])+"&qs=n&form=Z9LH5&sp=-1&pq="+str(key_word[i])
            html = get_one_page(url)
            # word_mean = get_word_mean(html)
            # word_cixing = get_part_of_speech(html)
            phrase = get_code_to_Phrase(html)
            word_phrase = get_word_phrase(phrase)
            print(word_phrase)
            # cixing = get_word_cixing(word_cixing)
            # pronucation = get_word_pronucation(key_word[i])
            # word_meaning = get_word_meaning(i,key_word[i],word_mean,cixing)
            # print(word_meaning)
            # parse_one_page(i,key_word[i],pronucation,word_meaning,word_phrase)

        except Exception:
            footer.write(i,0,key_word[i])
            wrongword.save('error_word.xls')
            print("处理异常，请检查.............................")

if __name__ == "__main__":
    main()