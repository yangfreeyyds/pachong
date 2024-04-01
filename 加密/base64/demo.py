import requests
import re
import base64
from fontTools.ttLib import TTFont # pip install fontTools

#这个实验网址老了
url = 'http://shanzhi.spbeen.com/login/?next=/detail/%3Fid%3D3139'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}

response = requests.get(url, headers=headers)

patternstr = "base64,(.*?)'"
results = re.findall(patternstr, response.text)


if results:
    base64str = results[0]
    print(base64str)
    fontfile_content = base64.b64decode(base64str)
    print(fontfile_content)
    with open('demo.ttf','wb') as f:
        f.write(fontfile_content)
    font = TTFont('demo.ttf')
    font.saveXML('demo.xml')

else:
    print("没有内容")
    base64str = ""