import datetime
import json
import re
import requests
 
stoday = datetime.datetime.now().strftime('%Y-%m-%d')


response = requests.get(
        'https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items')
html = response.json()['data'][0]['content']
cmd = r'data-pid="[^"]*">(\d+、[^；]*)；</p>'
results = re.findall(cmd, html, re.S)

print(results)
# return '\n\n'.join(results).replace('"', '"')