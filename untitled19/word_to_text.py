import pandas as pda
import docx

file1 = "D:\\English_text.docx"
document = docx.Document()

#读取excel表中的数据
file="D:\\12121212.xlsx"
data = pda.read_excel(file)
data = data.values.tolist()

word = []
for item in data:
    word.append(item[0])

document.add_paragraph(item1+" " for item1 in word)

document.save(file1)