import docx
from PIL import Image
import requests
file = docx.Document()
img = "http://localhost:8081/image/1.png"
img_name = img.split('/')[-1]
with open(img_name,'wb')as f:
    response = requests.get(img).content
    f.write(response)
    f.close()
file.add_picture(img_name)
file.save("D:\\my_picture.docx")