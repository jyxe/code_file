import re
import pandas as pda
import csv

print("please input the file_name:",end="")
file_name = input()
fileName="D:\\job_data"+"\\"+str(file_name)+".csv"

def get_word_from_html(html):
    parttern = re.compile('<td.*?>.*?</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>',re.S)
    items = re.findall(parttern,html)
    number = 1
    words = []
    for item in items:
        yield {
            "a_word":item[0],
            "b_alphabet":item[1],
            "c_meaning":item[2]
        }
        words.append(item)
        data = pda.DataFrame(words)
        # print(words)

    try:
        if number == 1:
            csv_headers = ['a_word', 'b_alphabet', 'c_meaning']
            data.to_csv(fileName, header=csv_headers, index=False, mode='a+', encoding='utf-8')
        else:
            data.to_csv(fileName, header=False, index=False, mode='a+', encoding='utf-8')
            number = number + 1
    except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

def main():
    html=""""""

    items = get_word_from_html(html)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()