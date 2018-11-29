# -*- coding: utf-8 -*-
import subprocess
import time
from py2neo import Graph

graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")
name = "2018_shanxi_gaokao.tex"
path = "D:\\"+str(name)
f_name = open(path, 'w+', encoding="utf-8")

def read_data_from_database(cypher):
    data = graph.run(cypher).to_data_frame()
    data = data.values.tolist()
    data_math = []
    for i in range(len(data)):
        # print(data[i][0])
        data_math.append(data[i][0])

    return data_math

def wirte_to_latex_file(content):
    tex_content=["\documentclass[UTF8]{article}","\\usepackage{CTEX}","\\usepackage{graphicx, subfig}","\\renewcommand{\\baselinestretch}{2.0}","\\usepackage[tmargin=1cm,lmargin=1cm]{geometry}","\\usepackage{float}","\\usepackage{multirow}","\\begin{document}"]
    for j in range(len(tex_content)):
        print(tex_content[j])
        f_name.write(tex_content[j])
        f_name.write("\n")
    for i in range(len(content)):
        print(content[i])
        f_name.write(content[i])
        f_name.write("\n")
        f_name.write("\n")

    f_name.write("\end{document}")
    f_name.close()
    time.sleep(2)

def main():
    cypher = ("match (n:physical2) return n.content")
    data = read_data_from_database(cypher)
    wirte_to_latex_file(data)

    cmd = "pdflatex D:/" + str(name)
    s = subprocess.Popen(cmd, shell=True)
    while True:
        if s.poll() is not None:
            break
if __name__ == '__main__':
    main()