import requests


def login(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    resonpse = requests.get(url, headers=headers)
    print(resonpse.status_code)
    open('./bokeyuan.html', "wb").write(resonpse.content)


if __name__ == '__main__':
    login("https://www.cnblogs.com/")
