
# &#x9ea3;&#x9f92;&#x9fa4;&#x9f92;&#x9f92;
# 10400

import requests

fonturl = 'http://shanzhi.spbeen.com/static/fonts/szec.ttf'
fontresponse = requests.get(fonturl)
print(fontresponse)
with open('font.ttf', 'wb') as file:
    file.write(fontresponse.content)


url = 'http://shanzhi.spbeen.com/search/?word='
response = requests.get(url)
print(response.text)