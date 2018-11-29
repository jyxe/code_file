from py2neo import Graph,Node,Relationship
import docx
import csv
from selenium import webdriver
from win32com import client

#连接neo4j数据库
graph = Graph("bolt://localhost:7687",username="neo4j",password="13820541017")

#创建word文档
file = docx.Document()
file.add_paragraph("******************************  北京雄恩教育研发中心研发  *******************************"+"\n")

#建立函数从数据数据库中上传数据,当需要同时上传单词数据和文章数据时请使用本函数
# def upload_data_to_database(cypher_word,cypher_text):
#     graph.run(cypher_word)
#     graph.run(cypher_text)

#只上传文章不上传单词时使用本函数
def upload_data_to_database1(cypher_text):
    graph.run(cypher_text)

#只上传单词不上传内容时使用本函数
# def upload_data_to_database2(cypher_word):
#     graph.run(cypher_word)

#定义函数读取数据库中的文章数据
def read_text_from_database(cypher):
    text_data_list = []
    text_data = graph.run(cypher).to_data_frame()
    text_data = text_data.values.tolist()

    items = " ".join(sorted(set(text_data)))
    item = items.split()

    for i in range(len(item)):
            if (len(item[i])>2 and len(item[i])<18):
                # print(item[i])
                text_data_list.append(item[i])

    return text_data_list

def read_word_from_database(cypher):
    word_data_list = []
    word_data = graph.run(cypher).to_data_frame()
    word_data = word_data.values.tolist()

    for item in word_data:
        word_data_list.append(item)

    return word_data_list

def main():
    cypher = ("load csv with headers from 'file:/beijing2016.csv' as row create (n:text000) set n=row")
    cypher1 = ("match (n:text000) return n.a_reading,n.b_answer")
    cypher2 = ("match (n:word6) return n.a_word,n.b_alphabet,n.c_meaning")
    upload_data_to_database1(cypher)
    data = read_text_from_database(cypher1)
    print("********************************text*****************************")
    print(data[0][0])

    data1 = read_word_from_database(cypher2)
    print("*******************************word******************************")
    print(data1[0][0])

if __name__ == "__main__":
    main()


