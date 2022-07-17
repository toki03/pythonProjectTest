import requests
from bs4 import BeautifulSoup


def login(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    open('./result/bokeyuan.html', "wb").write(response.content)
    result = response.text
    soup = BeautifulSoup(result, "html.parser")
    text_find = soup.find_all(attrs='a', class_="post-item-title")
    print(type(text_find))
    for i in text_find:
        print("链接地址: ", i['href'], "文本：", i.get_text())


def login_weibo(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    sess = requests.session()
    response = sess.get(url, headers=headers)
    print(response.status_code)
    open('./result/bokeyuan.html', "wb").write(response.content)


if __name__ == '__main__':

    # login("https://www.cnblogs.com/")
    login_weibo('https://weibo.com/u/page/follow/6668389510')
