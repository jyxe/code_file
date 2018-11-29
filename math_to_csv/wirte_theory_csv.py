import pandas as pda
import csv

file = "D:\\theory.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
print(data1)

def write_to_csv():

    th_ID1 = []
    define1 =  []
    content1 = []
    core_ID1 = []
    con_ID1 = []
    ch_D1 = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\theory3.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")

    for item in data1:
        yield {
            "th_ID":item[0],
            "define":item[1],
            "content":item[2],
            "core_ID":item[3],
            "con_ID":item[4],
            "ch_D":item[5]
        }
        th_ID1.append(item[0])
        define1.append(item[1])
        content1.append(item[2])
        core_ID1.append(item[3])
        con_ID1.append(item[4])
        ch_D1.append(item[5])

    writer = csv.writer(csvfile)

    header = ['th_ID','define','content','core_ID','con_ID','ch_ID']

    writer.writerow(header)
    writer.writerows(zip(th_ID1, define1, content1,core_ID1,con_ID1,ch_D1))

def main():
    data = write_to_csv()
    for item in data:
        print(item)

if __name__ == "__main__":
    main()