import pandas as pda
import csv

file = "D:\\beijing_2018.xlsx"
data = pda.read_excel(file,enconding="utf-8")
data1 = data.values.tolist()
content = []
for item in data1:
    content.append(item)

for i in range (len(content)):
    print(content[i][0])

file_name = 'D:\\neo4j-community\\neo4j-community-3.1.0\\import\\2018_beijing_gaokao9.csv'
csvfile = open(file_name, 'a+', newline='', encoding="utf-8")
writer = csv.writer(csvfile)
header = ['content']

writer.writerow(header)
writer.writerows(content)