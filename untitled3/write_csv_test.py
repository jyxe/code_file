import pandas as pda
import csv
from py2neo import Graph
import time
import subprocess

print("请输入文件名：", end="")
file_name = input()

def read_execl_data(file):
    print("********** 1 **************")
    data = pda.read_excel(file,enconding="utf-8")
    # 将读出来的数据进行转换转换为列表的形式，以便进行操作
    data = data.values.tolist()
    content = []
    for item in data:
        content.append(item)

    return content

#将读出来的数据写入csv文档
def write_content_to_csv(file_name,content):
    print("************ 2 **************")
    csvfile = open(file_name,'a+',newline='',encoding="utf-8")
    writer = csv.writer(csvfile)

    #写入头部信息
    header = ['content']
    writer.writerow(header)
    #写入内容
    if (content=="nan"):
        content = ""
        writer.writerows(content)
    else:
        writer.writerows(content)

def main():
    # 定义excel表的位置
    file_excel = "D:\\" + str(file_name) + ".xlsx"
    content = read_execl_data(file_excel)

    # 定义存储的csv表的位置，然后将excel读出来的数据写入csv表中
    file_csv = "D:\\neo4j-community\\neo4j-community-3.1.0\\import\\" + str(file_name) + ".csv"
    write_content_to_csv(file_csv,content)

if __name__ == "__main__":
    main()