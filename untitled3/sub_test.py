import pandas as pda
import csv
from py2neo import Graph
import subprocess
import time

#链接数据库
graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

#从excel中读取数据
def read_data_from_excel(file_path):
    print("********************** 1 *********************")
    data = pda.read_excel(file_path)
    data = data.values.tolist()
    content=[]
    for item in data:
        content.append(item)
    return content

#将excel读入的数据存储到csv文件
def write_content_to_csv(file_name,content):
    print("********************** 2 *********************")
    csvfile = open(file_name,'a+',newline='',encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['a_content','b_answer_A','b_answer_B','b_answer_C','b_answer_D']
    writer.writerow(header)
    writer.writerows(content)

#将csv数据上传到数据库
def load_csv_to_database(cypher):
    print("********************** 3 *********************")
    graph.run(cypher)

#读取数据库中的数据
def read_data_from_database(cypher):
    print("********************** 4 *********************")
    data = graph.run(cypher).to_data_frame()
    data = data.values.tolist()
    # content = []
    # for i in range(len(data)):
    #     for j in range(5):
    #         content.data[i][j]
    return data

#将读取的数据写入latex文档
def write_content_to_latex(latex_file,content):
    print("********************** 5 *********************")
    tex_content = ["\documentclass[UTF8]{article}", "\\usepackage{CTEX}", "\\usepackage{graphicx, subfig}",
                   "\\renewcommand{\\baselinestretch}{2.0}", "\\usepackage[tmargin=1cm,lmargin=1cm]{geometry}",
                   "\\usepackage{float}", "\\usepackage{multirow}", "\\begin{document}"]
    for j in range(len(tex_content)):
        # print(tex_content[j])
        latex_file.write(tex_content[j])
        latex_file.write("\n")
    k=1
    for i in range(len(content)):
        for j in range(5):

            if(i==0 and j==0):
                    latex_file.write("\\begin{center}\\textbf{\Large"+content[i][j]+"}\end{center}")
            elif(j==0):
                if(len(content[i][j])<5):
                    latex_file.write("\\begin{center} "+content[i][j]+"\end{center}")

                elif(len(content[i][j])>50):
                    latex_file.write("\par "+content[i][j])

                else:
                    latex_file.write("\n")
                    latex_file.write("\n")
                    latex_file.write("\\noindent "+str(i-4)+". "+content[i][j])
                    latex_file.write("\n")
                    latex_file.write("\n")
                    k += 1
            else:
                if (content[i][j] == "nan"):
                    content[i][j] = ""
                    latex_file.write(content[i][j])

                elif(j==1):
                    latex_file.write("\\noindent "+content[i][j]+"$\qquad$ $\qquad$")
                elif(j==2):
                    latex_file.write(content[i][j]+"$\qquad$")
                    latex_file.write("\n")
                    latex_file.write("\n")
                elif (j == 3):
                    latex_file.write("\\noindent " + content[i][j] + "$\qquad$ $\qquad$")
                elif (j == 4):
                    latex_file.write(content[i][j] + "$\qquad$")
                    latex_file.write("\n")
                    latex_file.write("\n")

    latex_file.write("\end{document}")
    latex_file.close()
    time.sleep(2)

#定义主函数main()
def main():
    print("请输入文件名字:",end="")
    file_name = input()
    file_path = "D:\\"+str(file_name)+".xlsx"
    content = read_data_from_excel(file_path)

    #定义存储的csv文件的路径
    csv_file = "D:\\neo4j-community\\neo4j-community-3.1.0\\import\\"+str(file_name)+".csv"
    write_content_to_csv(csv_file,content)

    #定义cypher语句将数据上传到数据库
    cypher1=("load csv with headers from 'file:/"+str(file_name)+".csv' as row create(n:"+str(file_name)+") set n=row")
    load_csv_to_database(cypher1)

    #定义cypher语句从数据库中读取数据
    cypher2=("match (n:"+str(file_name)+") return n.a_content,n.b_answer_A,n.b_answer_B,n.b_answer_C,n.b_answer_D")
    content1 = read_data_from_database(cypher2)
    # print(content1)

    #生成latex文档，并将数据库写入latex，然后生成pdf
    path = "D:\\" + str(file_name) + ".tex"
    f_name = open(path, 'w+', encoding="utf-8")
    write_content_to_latex(f_name, content1)

    cmd = "pdflatex D:/" + str(file_name) + ".tex"
    s = subprocess.Popen(cmd, shell=True)
    s.communicate()

if __name__ == "__main__":
    main()
