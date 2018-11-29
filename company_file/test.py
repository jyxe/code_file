import re
import pandas as pda
import csv

fileName="word_to_csv.csv"

print("请输入修改后的文件名称：",end="")
fix_file_name = input()

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

    words_word = []
    words_alphabet = []
    words_meaning = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\' + str(fix_file_name) + '.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")

    data = pda.read_csv(fileName)
    data = data.values.tolist()

    for item in data:
        yield {
            "a_word": item[0],
            "b_alphabet": item[1],
            "c_meaning": str(item[2]).replace('\r\n', '   ')
        }
        words_word.append(item[0])
        words_alphabet.append(item[1])
        words_meaning.append(str(re.compile(r'<[^>]+>', re.S).sub('', str(item[2]))).replace('\r\n', '   '))

    writer = csv.writer(csvfile)
    # 当需要继续往同一张表中添加数据时，一定要注释掉此行
    header = ['a_word', 'b_alphabet', 'c_meaning']

    # 当需要继续往同一张表中添加数据时，一定要注释掉此行
    writer.writerow(header)
    writer.writerows(zip(words_word, words_alphabet, words_meaning))

def main():
    html="""
             <tr>
                <td class="export-td">3052</td>
                <td class="export-td">immortal</td>
                <td class="export-td">英:/ɪ'mɔːt(ə)l/ 美:/ɪ'mɔrtl/ </td>
                <td class="export-td">1. adj. 长生的；不朽的；神仙的
2. n. 不朽人物；神仙</td>
            </tr>
"""

    items = get_word_from_html(html)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()