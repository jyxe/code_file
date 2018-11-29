import pandas as pda
import csv

file = "G:\\math\\concept.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    number_ID = []
    define = []
    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\concept123_relation.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['con_ID','define']
    writer.writerow(header)

    for item in data1:
        number_ID.append(item[0])
        define.append(item[1])
        # print(item[0])
    writer.writerows(zip(number_ID,define))

def main():
    write_to_csv()

if __name__ == "__main__":
    main()