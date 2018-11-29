import pandas as pda
import csv

file = "D:\\math_data\\excersise.xlsx"

data = pda.read_excel(file,encoding="utf-8")
data1 = data.values.tolist()
# print(data1)

def write_to_csv():
    exercise_num = []
    content = []

    file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\exercise_relation.csv'
    csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
    writer = csv.writer(csvfile)
    header = ['exercise_num','content']
    writer.writerow(header)

    for item in data1:
        exercise_num.append(item[0])
        content.append(item[1])
        # print(item[0])
    writer.writerows(zip(exercise_num,content))

def main():
    write_to_csv()

if __name__ == "__main__":
    main()