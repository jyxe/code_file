import requests
import urllib3
import re
urllib3.disable_warnings()
import pandas as pda
import xlwt

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('word',cell_overwrite_ok=True)
# conn = pymysql.connect(host="localhost",user="root",passwd="root",db="word1",charset="utf8")
path = "D:\\job_data\\1.xlsx"

def get_data():
    word=[]
    data = pda.read_excel(path)
    data = data.values.tolist()
    for i in range(len(data)):
        print(data[i][0])
        word.append(data[i][0])
    return word

#获取网站源码
def get_html_from_website(url):
    response = requests.get(url,verify=False)
    if response.status_code==200:
        return response.text

    else:
        print("网页浏览异常.....................")

#提取代码中的信息
def parase_one_page(html):
    parttern = re.compile('<span class="bil">(.*?)</span>.*?<span class="val">(.*?)</span>',re.S)
    items = re.findall(parttern,html)
    return items

def main():
    key_word=get_data()

    for i in range(len(key_word)):
        k=1
        word = []
        url="https://cn.bing.com/dict/search?q="+str(key_word[i])+"&qs=n&form=Z9LH5&sp=-1&pq="+str(key_word[i])
        html = get_html_from_website(url)
        # print(html)
        # print("***********************" + str(key_word[i]) + "****************************************")
        print("\n")
        items = parase_one_page(html)

        for item in items:
            word.append(item[0]+" "+item[1])

        for x in word:
            content = " ".join([str(k)+". "+str(x)])
            k+=1
        # content = ' '.join([str(k)+str(x)+"\n" for x in word])
            print(content)
    #     for k in range(2):
    #         if(k==0):
    #             worksheet.write(i,k,key_word[i])
    #         else:
    #             worksheet.write(i, k, content)
    #     # print(str(content))
    # workbook.save('data.xls')

if __name__ =="__main__":
    main()