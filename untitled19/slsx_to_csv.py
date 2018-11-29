import pandas as pda
import csv

file = "D:\\job_data\\word_z_v.xls"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    a_word = []
    b_alphabet = []
    c_mean = []
    d_phrase = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\word_oxford2.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['a_word','b_alphabet','c_mean','d_phrase']
    writer.writerow(header)

    for item in data1:
        a_word.append(item[0])
        b_alphabet.append(item[1])
        c_mean.append(item[2])
        d_phrase.append(item[3])

    writer.writerows(zip(a_word,b_alphabet,c_mean,d_phrase))

def main():
    write_to_csv()

if __name__ == "__main__":
    main()