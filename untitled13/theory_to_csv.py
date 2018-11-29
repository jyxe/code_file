import pandas as pda
import csv

file = "D:\\math_data\\theory.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    define = []
    content = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\theory_relation.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['define','content']
    writer.writerow(header)

    for item in data1:
        define.append(item[0])
        content.append(item[1])
        # print(item[0])
    writer.writerows(zip(define,content))

def main():
    write_to_csv()

if __name__ == "__main__":
    main()