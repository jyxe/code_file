import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url="https://fanyi.baidu.com/v2transapi"
headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'from':'en',
    'to':'zh',
    'query':'well',
    'transtype':'translang',
    'simple_means_flag':'3'
}

response = requests.post(url,data=data,headers=headers,verify=False)
print(response.json())