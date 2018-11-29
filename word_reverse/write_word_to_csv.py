#编写此程序的时候遇到的问题是：当从csv中获取的数据被抓取下来时，显示的顺序并不是自己想要的。
# 经过反复试验发现原来从数据库获取的数据，他的显示顺序是按照定义的表头的字母顺序来显示的，如word，number就出现在alphabet
#之后，我的解决方案是将csv表格的头部重新命名为:'a_order', 'b_word','c_alphabet','d_meaning'这样就按照正常的顺序显示了,
#还有就是我如何遍历数据库中的数据的时候，在遍历所有的行和列时遇到的问题就是没有办法遍历，最后我的解决方案就是把它转换为列表，
#然后在添加生成器yield，然后开始遍历最后在插入到csv文件中去。这样就实现了数据的存储
import pymysql
import pandas as pda
import traceback

#链接数据库
conn = pymysql.connect(host="localhost",user="root",password="root",db="dict_oxford_primary",charset="utf8")
fileName = 'word_oxford_primary.csv'

#从数据库获取数据
def get_data_from_database(sql):
    data = pda.read_sql(sql,conn)
    data = data.values.tolist()
    return data

#生成迭代对象，并且写入csv格式的文档中
def write_to_csv(content):
    words = []
    number = 1
    for item in content:
        yield {
            "word1":item[0],
            "alphabet":item[1],
            "meaning":item[2]
        }
        words.append(item)
        data = pda.DataFrame(words)
        # print(words)
    try:
        if number == 1:
           csv_headers = ['a_word','b_alphabet','c_meaning']
           data.to_csv(fileName, header=csv_headers, index=False, mode='a+', encoding='utf-8')
        else:
           data.to_csv(fileName, header=False, index=False, mode='a+', encoding='utf-8')
           number = number + 1
    except UnicodeEncodeError:
           print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

def main():
    sql="select * from word_list"
    data = get_data_from_database(sql)
    print(data)
    for word in write_to_csv(data):
        print(word)

if __name__ == "__main__":
    main()