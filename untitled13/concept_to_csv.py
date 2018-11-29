import pandas as pda
import csv

file = "D:\\math_data\\conception.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    ex_ID1 = []
    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\conception_relation.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['concept']
    writer.writerow(header)

    for item in data1:
        ex_ID1.append(item)
        print(item[0])
    writer.writerows(ex_ID1)

def main():
    write_to_csv()

if __name__ == "__main__":
    main()