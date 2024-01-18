import requests
from bs4 import BeautifulSoup
import time
 
my_dict = {
    "1": "4Kxinnian",
    "2": "4Kdujia",
    "3": "4kyouxi",
    "4": "4kdongman",
    "5": "4kmeinv",
    "6": "4kfengjing",
    "7": "4kyingshi",
    "8": "4kqiche",
    "9": "4kdongwu",
    "10": "4kbeijing",
    "11": "pingban",
    "12": "shoujibizhi",
}
 
 
def get_spec_pages(bizhi_type):
    page_total = 1
    for i in range(page_total):
        get_single_page(i, bizhi_type)
 
 
def get_single_page(page, bizhi_type=""):
    try:
        page = int(page)
    except ValueError:
        return False
    while True:
        if page == 0:
            pic_list_url = 'https://pic.netbian.com/{}/index.html'.format(bizhi_type)
        else:
            pic_list_url = 'https://pic.netbian.com/{}/index_{}.html'.format(bizhi_type, page)
        Myheaders = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        #req = requests.session()
        pic_list_html = requests.get(pic_list_url, headers = Myheaders)
        pic_list_html.encoding = 'gbk'
        soup = BeautifulSoup(pic_list_html.text,'lxml')
        pic_lists = soup.find('ul',{'class' : 'clearfix'}).find_all('li')
 
        x = 1
        for li in pic_lists:
            pic_url = 'https://pic.netbian.com/' + li.a.get('href')
 
            pic_html = requests.get(pic_url,headers = Myheaders)
            pic_html.encoding = 'gbk'
 
            sp = BeautifulSoup(pic_html.text,'lxml')
 
            pic_download = 'https://pic.netbian.com/' + sp.find('a',{'id' : 'img'}).img.get('src')
            #获取返回的字节类型
            img = requests.get(pic_download, headers=Myheaders).content
            path = str(sp.find('a',{'id' : 'img'}).img.get('title')) + ".jpg"
 
            with open(path, 'wb') as f:
                    f.write(img)
                    time.sleep(1)
                    print("第【{}】页第【{}】张图片下载完成！".format(page+1,x))
                    x += 1
 
        page += 1
        if page == 15:
            print('下载结束！')
            break
 
def main():
    # 打印带序号的字符串供用户选择
    for i, (key, value) in enumerate(my_dict.items(), start=1):
        print(f"{key}: {value}")
 
    # 等待用户输入序号
    choice = input("请输入要下载的序号：")
 
    # 根据用户输入的序号查找字典中的值并拼接成字符串
    if choice.isdigit():
        index = int(choice)
        selected_key = list(my_dict.keys())[index - 1]  # 索引从0开始，所以要减1
        selected_value = my_dict[selected_key]
        result = f"{selected_key}: {selected_value}"
        get_spec_pages(selected_value)
    else:
        print("无效的序号，请输入一个正整数。")
 
if __name__ == '__main__':
    main()