import pandas as pda
import csv
import os
import re

print("请输入您要读取的csv文件的名字，不需要添加后缀：",end="")
read_file_name = input()

print("请输入修改后的文件名称：",end="")
fix_file_name = input()

data = pda.read_csv("D:\job_data"+"\\"+str(read_file_name)+".csv")
data = data.values.tolist()

def get_data_from_database():
    words_word = []
    words_alphabet = []
    words_meaning = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\'+str(fix_file_name)+'.csv'
    csvfile = open(file_name, 'a+', newline='',encoding="utf-8")

    for item in data:
        yield {
            "a_word":item[0],
            "b_alphabet":item[1],
            "c_meaning":str(item[2]).replace('\r\n','   ')
        }
        words_word.append(item[0])
        words_alphabet.append(item[1])
        words_meaning.append(str(re.compile(r'<[^>]+>',re.S).sub('',str(item[2]))).replace('\r\n','   '))

    writer = csv.writer(csvfile)
    #当需要继续往同一张表中添加数据时，一定要注释掉此行
    header = ['a_word', 'b_alphabet','c_meaning']

    #当需要继续往同一张表中添加数据时，一定要注释掉此行
    writer.writerow(header)
    writer.writerows(zip(words_word,words_alphabet,words_meaning))

def main():
    items = get_data_from_database()
    for item in items:
        print(item)

if __name__ == "__main__":
    main()