import requests
url = 'http://res.iciba.com/resource/amp3'


response = requests.get(url)
with open('1.mp3','wb') as f:

#因为是mp3文件，所以用content

    f.write(response.content)
