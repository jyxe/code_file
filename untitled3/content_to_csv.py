import pandas as pda
import csv
from py2neo import Graph
import subprocess
import time

graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")
print("请输入文件名：", end="")
file_name = input()

#定义函数从excel中读取数据
def read_date_from_excel(file):
    print("********************** 1 *********************")
    data = pda.read_excel(file,enconding="utf-8")
    data1 = data.values.tolist()
    content = []
    for item in data1:
        content.append(item)
    # print(content)
    return content

#将excel表中读出来的数据存入csv表中
def write_content_to_csv(file_name,content):
    print("********************** 2 *********************")
    # for i in range (len(content)):
    #     for j in range(6):
    #         print(content[i][j])

    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['a_content','b_image','c_answer_A','c_answer_B','c_answer_C','c_answer_D']
    writer.writerow(header)
    writer.writerows(content)

#上传写好的csv数据到数据库：
def load_csv_to_database(cypher):
    print("********************** 3 *********************")
    graph.run(cypher)

#从数据库中读取数据
def get_data_from_database(cypher):
    print("********************** 4 *********************")
    data = graph.run(cypher).to_data_frame()
    data = data.values.tolist()
    #     for i in range(len(data)):
    # for j in range(5):
    #         if data[i][j]=="nan":
    #             data[i][j]=""
    #             print(data[i][j])
    return data

#将读取出来的数据写到latex当中去
def write_content_to_latex(latex_file,content):
    k=1
    print("********************** 5 *********************")
    tex_content = ["\documentclass[UTF8]{article}", "\\usepackage{CTEX}", "\\usepackage{graphicx, subfig}",
                   "\\renewcommand{\\baselinestretch}{2.0}", "\\usepackage[tmargin=1cm,lmargin=1cm]{geometry}",
                   "\\usepackage{float}", "\\usepackage{multirow}", "\\begin{document}"]
    for j in range(len(tex_content)):
        # print(tex_content[j])
        latex_file.write(tex_content[j])
        latex_file.write("\n")
    for i in range(len(content)):
        for j in range(6):
            print(content[i][j])
            if(j==0):
                latex_file.write("\n")
                latex_file.write("\n")
                latex_file.write(str(k)+"."+content[i][j])
                latex_file.write("\n")
                latex_file.write("\n")
                k+=1
            elif(j==1):
                if(content[i][j]=="nan"):
                    content[i][j]=""
                    latex_file.write(content[i][j])
                else:
                    latex_file.write("\\begin{figure}[H]")
                    latex_file.write("\n")
                    latex_file.write("\centering")
                    latex_file.write("\n")
                    latex_file.write("\includegraphics[scale=0.8]{D:/"+str(content[i][j])+"}")
                    latex_file.write("\n")
                    latex_file.write("\end{figure}")
                    latex_file.write("\n")

            else:
                if(len(content[i][j]))<15:
                    if(content[i][j]=="nan"):
                        content[i][j]=""
                        latex_file.write(content[i][j])
                    else:
                        latex_file.write(content[i][j])
                        latex_file.write("$\qquad$ $\qquad$")
                else:
                    latex_file.write(content[i][j])
                    latex_file.write("\n")
                    latex_file.write("\n")

    latex_file.write("\end{document}")
    latex_file.close()
    time.sleep(2)

def main():
    #定义csv表的位置
    file_excel = "D:\\"+str(file_name)+".xlsx"
    content = read_date_from_excel(file_excel)

    #定义存储的csv表的位置，然后将excel读出来的数据写入csv表中
    file_csv = "D:\\neo4j-community\\neo4j-community-3.1.0\\import\\"+str(file_name)+".csv"
    write_content_to_csv(file_csv,content)

    #定义cypher语句将数据上传到数据库
    cypher=("load csv with headers from 'file:/"+str(file_name)+".csv' as row create(n:"+str(file_name)+") set n=row")
    load_csv_to_database(cypher)

    #定义cypher语句从数据库中读取数据
    cypher=("match (n:"+str(file_name)+") return n.a_content,n.b_image,n.c_answer_A,n.c_answer_B,n.c_answer_C,n.c_answer_D")
    content = get_data_from_database(cypher)

    #生成latex文档，并将数据库写入latex，然后生成pdf
    path = "D:\\" + str(file_name) + ".tex"
    f_name = open(path, 'w+', encoding="utf-8")
    write_content_to_latex(f_name, content)

    cmd = "pdflatex D:/" + str(file_name) + ".tex"
    s = subprocess.Popen(cmd, shell=True)
    while True:
        if s.poll() is not None:
            break

if __name__ == "__main__":
    main()