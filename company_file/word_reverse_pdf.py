# -*- encoding: utf-8 -*-
import  os
from selenium import webdriver
from win32com import client

print("请输入pdf文档的名字(以英文命名,不需要后缀)：", end="")
FTP_NAME = input()

browser = webdriver.Chrome()
def doc_to_pdf(doc_name, pdf_name):

    try:
        word = client.DispatchEx("Word.Application")
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        worddoc = word.Documents.Open(doc_name,ReadOnly = 1)
        worddoc.SaveAs(pdf_name, FileFormat = 17)
        worddoc.Close()
        return pdf_name
    except:
        return 1

def main():
    doc_name = "D:\\wooo.docx"
    ftp_name = "D:\\python_web_server\\"+str(FTP_NAME)+".pdf"
    doc_to_pdf(doc_name, ftp_name)
    browser.get("http://localhost:8081/"+str(FTP_NAME)+".pdf")

if __name__=='__main__':
    main()
