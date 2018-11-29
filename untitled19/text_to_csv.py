import pandas as pda
import csv

file = "D:\\job_data\\English_text.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    a_Reading = []
    b_Answers = []


    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\English_text2.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['a_Reading','b_Answers']
    writer.writerow(header)

    for item in data1:
        a_Reading.append(item[0])
        b_Answers.append(item[1])

    writer.writerows(zip(a_Reading,b_Answers))

def main():
    write_to_csv()

if __name__ == "__main__":
    main()