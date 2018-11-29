import docx

file = docx.Document("D:\\English.docx")
for paragrah in file.lines:
    print(paragrah.text)