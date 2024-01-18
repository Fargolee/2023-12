
import requests
 
# 定义钉钉机器人的Webhook地址
webhook_url = "https://oapi.dingtalk.com/robot/send?access_token="
 
def send_message(content):
    # 构造POST请求的payload
    payload = {
        'msgtype': 'text',
        'text': {'content': content}
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        
        if response.status_code == 200:
            print("消息已成功发送")
        else:
            print("消息发送失败")
            
    except Exception as e:
        print("发生错误：", str(e))
 
# 调用函数发送消息
send_message("这是我通过Python钉钉机器人发送的测试消息！")