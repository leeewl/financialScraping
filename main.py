import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


def get_gold_data():
    url = 'http://quote.eastmoney.com/q/118.iAu999.html'
    response = requests.get(url, headers)
    html = response.text
    print(html)

def get_data():
    get_gold_data()

if __name__ == '__main__':
    while(True):
        command = input("请输入需要的操作\n1,获取信息\nq,退出")
        if command == 'q':
            break
        elif command == '1':
            get_data()
        else:
            print("error input!!!\n\n")
