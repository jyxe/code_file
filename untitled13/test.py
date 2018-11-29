import pandas as pda
import csv

file = "D:\\English_data1.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    word = []
    alphabet = []
    content = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\word_test11.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['a_word','b_alphabet','content']
    writer.writerow(header)

    for item in data1:
        word.append(item[0])
        alphabet.append(item[1])
        content.append(item[2])

        # print(item[0])
    writer.writerows(zip(word,alphabet,content))

def main():
    write_to_csv()

if __name__ == "__main__":
    main()