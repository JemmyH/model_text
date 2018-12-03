# _*_ coding:utf-8 _*_
import requests
import urllib.request
headers = {}
headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'


def requests_test(url):
    response = requests.get(url, timeout=20, headers=headers)  # 返回一个response对象
    print(response.status_code)  # 状态码
    print(response.encoding)  # 网页编码格式
    print(response.url)  # 产生响应的url
    print(response.headers)  # response的头部信息
    print(response.cookies)  # cookies
    print(response.text)  # 以文本形式返回页面html代码
    print(response.content)  # 以字节流格式返回页面html代码
    print(response.history)


if __name__ == '__main__':
    url = "http://img.mmjpg.com/2015/12/9.jpg"
    # payload = {'spm_id_from': '333.334.primary_menu.81'}
    requests_test(url)  # 以问号的形式传递参数
    # urllib.request.urlretrieve("http://img.mmjpg.com/2015/12/9.jpg","F:\\image\\1.jpg")
