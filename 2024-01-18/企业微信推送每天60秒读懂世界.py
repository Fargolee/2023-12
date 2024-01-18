import datetime
import json
import re
import requests
 
stoday = datetime.datetime.now().strftime('%Y-%m-%d')
api_url = 
headers = {"Content-Type": "'application/json;charset=utf-8'"}
 
def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
    }
    # requests.post(api_url,json.dumps(json_text),headers=headers, timeout=9)
    rtxt = requests.post(api_url,json.dumps(json_text),headers=headers, timeout=9).json()
    return rtxt['errcode'] == 0 and rtxt['errmsg'] == 'ok'
 
 
def news_60s():
    response = requests.get(
        'https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items')
    html = response.json()['data'][0]['content']
    cmd = r'data-pid="[^"]*">(\d+、[^；]*)；</p>'
    results = re.findall(cmd, html, re.S)
    results.insert(0, f'{stoday} · 60秒新闻')
    return '\n\n'.join(results).replace('"', '"')
 
 
if __name__ == '__main__':
    news = news_60s()
    #print(len(news))
    if len(news) > 737 :
        news1 = news[0:737]
        news2 = news[737:]
        print(msg(news1))
        print(msg(news2))
    else:
        #print(news)
        print(msg(news))