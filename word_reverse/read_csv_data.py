import pandas as pda
import csv
import os
import re
fileName = "word1.csv"
data = pda.read_csv("D:/word_oxford_primary.csv")
data = data.values.tolist()

def get_data_from_database():
    words_word = []
    words_alphabet = []
    words_meaning = []

    current_dir = os.path.abspath('.')
    file_name = os.path.join(current_dir, "word2.csv")
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