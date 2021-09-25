import requests


url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
txt = response.text

with open('webf.txt', 'w', encoding='utf-8') as f:
   f.write(txt)
