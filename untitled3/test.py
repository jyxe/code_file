import pandas as pda
import csv
from py2neo import Graph
import time
import subprocess

#链接数据库
graph=Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

#定义函数来读取excel中的数据
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
    writer.writerows(content)

#上传写好的csv数据到neo4j数据库中
def upload_csv_to_database(pypher):
    print("*************** 3 ****************")
    graph.run(pypher)

#读取neo4j数据库中的数据
def read_data_from_database(pypher):
    print("**************** 4 ***************")
    data = graph.run(pypher).to_data_frame()
    data = data.values.tolist()
    data_science = []
    for i in range(len(data)):
        data_science.append(data[i][0])

    return data_science

#将内容写入latex文档
def wirte_to_latex_file(latex_file,content):
    print("********************** 5 *********************")
    tex_content=["\documentclass[UTF8]{article}","\\usepackage{CTEX}","\\usepackage{graphicx, subfig}","\\renewcommand{\\baselinestretch}{2.0}","\\usepackage[tmargin=1cm,lmargin=1cm]{geometry}","\\usepackage{float}","\\usepackage{multirow}","\\begin{document}"]
    for j in range(len(tex_content)):
        print(tex_content[j])
        latex_file.write(tex_content[j])
        latex_file.write("\n")
    for i in range(len(content)):
        print(content[i])
        latex_file.write(content[i])
        latex_file.write("\n")
        latex_file.write("\n")

    latex_file.write("\end{document}")
    latex_file.close()
    time.sleep(2)

def main():
    # 定义Excel文件名字路径
    print("请输入要读取的excel数据：",end="")
    file_name = input()
    file = "D:\\"+str(file_name)+".xlsx"
    content = read_execl_data(file)

    #定义写入的csv文档的位置
    csv_file_name = "D:\\neo4j-community\\neo4j-community-3.1.0\\import\\"+str(file_name)+".csv"
    write_content_to_csv(csv_file_name,content)

    #定义cypher语言，用来上传csv数据到数据库
    cypher1 = ("load csv with headers from 'file:/"+str(file_name)+".csv' as row create (n:"+str(file_name)+") set n=row")
    upload_csv_to_database(cypher1)

    #定义cypher语言来读取数据库中的数据
    cypher2 = ("match (n:"+str(file_name)+") return n.content")
    data_science = read_data_from_database(cypher2)

    #创建latex文档，将数据库读取出来的数据写入latex文档
    path = "D:\\" + str(file_name)+".tex"
    f_name = open(path, 'w+', encoding="utf-8")
    wirte_to_latex_file(f_name,data_science)

    cmd = "pdflatex D:/" + str(file_name)+".tex"
    s = subprocess.Popen(cmd, shell=True)
    while True:
        if s.poll() is not None:
            break

if __name__ == "__main__":
    main()