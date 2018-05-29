# _*_ coding:utf-8 _*_
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
i = 0


def yunsite(url):
    try:
        html = requests.get(url, headers=headers, allow_redirects=False, timeout=10).text
        et = etree.HTML(html)
        img_url = et.xpath("//div[@class='content']/a[1]/img/@src")[0]
        print("图片url：" + img_url)
        html1 = requests.get(img_url, headers=headers, allow_redirects=False, timeout=10)
        global i
        i += 1
        if not os.path.exists("F:\\image\\test{0}.jpg".format(i)):
            with open("F:\\image\\test{0}.jpg".format(i), "wb") as f:
                f.write(html1.content)
                print("test{0}.jpg".format(i) + "下载成功")
    except Exception as e:
        print("出现异常：" + str(e))
    return url


def download(url):
    try:
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Referer': 'http://www.jlhz001.com/'}, allow_redirects=False, timeout=10)
        name = url.split("/")[-1]
        with open(name, "wb") as f:
            f.write(response.content)
            print("下载完成")
    except Exception as e:
        print("出现异常：" + str(e))


if __name__ == '__main__':
    # urls = ["http://www.mmjpg.com/mm/1300/" + str(i) for i in range(1, 31)]
    # for url in urls:
    #     print(url + "开始")
    #     print(yunsite(url) + "结束")
    download("https://u2.b0b1.com:10058/640/cf/cf1861ab4d63edf6a6a73a37d3bb7a060a4a6475.mp4?md5=t_Sk4NKQi9xjnslTBsCGOA&expires=1527595637")
