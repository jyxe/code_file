import requests
import json
url = "https://fanyi.baidu.com/basetrans"

query_str = input("请输入要翻译的内容：")

data = {
        "query":query_str,
        "from":"en",
        "to":"zh"}

headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",

        "Referer": "https://fanyi.baidu.com/?aldtype=16047&tpltype=sigma"
}

response = requests.post(url,data=data,headers=headers)

html_str = response.content.decode()#json字符串

#json数据交换格式，使用json之前需要导入
#把json字符串转化为Python类型
dict_ret = json.loads(html_str)
print(dict_ret)
# print(type(dict_ret))
ret = dict_ret["dict"]["symbols"][0]["ph_am_mp3"]
url_am="http://res.iciba.com/resource/amp3"+str(ret)
ret1 = dict_ret["dict"]["symbols"][0]["ph_en_mp3"]
url_em="http://res.iciba.com/resource/amp3"+str(ret1)

if(ret==''):
    print("没有美式发音")
else:
    response = requests.get(url_am)
    with open("G:\\word_am_fayin\\"+str(query_str)+"_am.mp3","wb") as f:
    #因为是mp3文件，所以用content
        f.write(response.content)

if(ret1==''):
    print("没有英式发音")
else:
    response1 = requests.get(url_em)
    with open("G:\\word_em_fayin\\"+str(query_str)+"_em.mp3","wb") as f:
    #因为是mp3文件，所以用content
        f.write(response1.content)
