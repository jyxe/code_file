from urllib import request,parse
import json

def fanyi(content):


    data={
        'kw':content
    }
    data=parse.urlencode(data)
    # print(len(data))
    base_url = 'http://fanyi.baidu.com/sug'

    # Post
    headers = {
        "Content-Length": len(data),  # 动态计算data长度
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    #字符串转bytes
    req=request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=headers,verify=False)
    response=request.urlopen(req)
    html=response.read()
    html=html.decode('utf-8')

    json_data=json.loads(html)#梳理成json格式
    print(json_data)

    #整理数据
    for item in json_data['data']:
        print(item['k'],item['v'])

if __name__=='__main__':

    content = input('请输入您要翻译的内容：')
    fanyi(content)