
import json
import sys
import requests


def get_daily_sentence():
    """
    爬取金山词霸每日一句

    """

    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    r = json.loads(r.text)
    content = r["content"]
    note = r["note"]
    fenxiang_img = r["fenxiang_img"]
    daily_sentence = content + "\n" + note +"\n" + fenxiang_img
    return daily_sentence



# api_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a6146a74-e5ba-4439-9fc6-4fcafe1b079d'

api_url= 
headers = {"Content-Type": "'application/json;charset=utf-8'"}

# data = {
#         "msgtype": "text",
#         "text": {
#                         "content": get_daily_sentence()
#         }
# }
# requests_url = requests.post(url, headers=headers, data=json.dumps(data))

def msg(text):
    text= '钉钉测试\n'+text
    json_text= {
        'msgtype': 'text',
        'text': {'content': text}
    }
    requests.post(api_url,json.dumps(json_text),headers=headers)

def send_message(content):
    # 构造POST请求的payload
    content= '钉钉测试\n'+content
    payload = {
        'msgtype': 'text',
        'text': {'content': content}
        ,"isAtAll":True
    }
    
    try:
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            print("消息已成功发送")
        else:
            print("消息发送失败")
            
    except Exception as e:
        print("发生错误：", str(e))

if __name__ == '__main__':
    send_message(get_daily_sentence())
