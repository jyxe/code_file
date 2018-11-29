import requests

url="https://fanyi.baidu.com/v2transapi"
html = requests.get(url)
print(html.json())