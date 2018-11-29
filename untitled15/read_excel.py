import pandas as pda
import numpy as npy
import requests
import json
import urllib3

urllib3.disable_warnings()

url = "https://fanyi.baidu.com/basetrans"

path1="D:\\job_data\\1.xlsx"
# path2="D:\\job_data\\2.xlsx"

word_1 = pda.read_excel(path1)
# word_2 = pda.read_excel(path2)

word_1 = word_1.values.tolist()
# word_2 = word_2.values.tolist()

# print(len(word_1))
# print(len(word_2))
word = []
# for j in range(len(word_2)):
#     word.append(word_2[j][0])
    # print(word_2[j][0])

for i in range(len(word_1)):
    word.append(word_1[i][0])
    # print(word_1[i][0])

for k in range(len(word)):
    query_str = word[k]
    data = {
        "query": query_str,
        "from": "en",
        "to": "zh"}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Referer": "https://fanyi.baidu.com/?aldtype=16047&tpltype=sigma"
    }

    response = requests.post(url, data=data, headers=headers,verify=False)
    html_str = response.content.decode()  # json字符串

    # json数据交换格式，使用json之前需要导入
    # 把json字符串转化为Python类型
    dict_ret = json.loads(html_str)
    print(dict_ret)
    ph_am = "美：["+dict_ret["dict"]["symbols"][0]["ph_am"]+"] "+"英:["+dict_ret["dict"]["symbols"][0]["ph_en"]+"]"
    print(ph_am)
    # print(type(dict_ret))
    # try:
    #     ret = dict_ret["dict"]["symbols"][0]["ph_am_mp3"]
    #     url_am = "http://res.iciba.com/resource/amp3" + str(ret)
    #     if (ret == ''):
    #         print("没有美式发音")
    #     else:
    #         response = requests.get(url_am)
    #         with open("G:\\word_am_fayin\\" + str(query_str) + "_am.mp3", "wb") as f:
    #             # 因为是mp3文件，所以用content
    #             f.write(response.content)
    # except Exception:
    #     print("异常........................")
    #
    # try:
    #     ret1 = dict_ret["dict"]["symbols"][0]["ph_en_mp3"]
    #     url_em = "http://res.iciba.com/resource/amp3" + str(ret1)
    #     if (ret1 == ''):
    #         print("没有英式发音")
    #     else:
    #         response1 = requests.get(url_em)
    #         with open("G:\\word_em_fayin\\" + str(query_str) + "_em.mp3", "wb") as f:
    #             # 因为是mp3文件，所以用content
    #             f.write(response1.content)
    #
    # except Exception:
    #     print("异常.......................")