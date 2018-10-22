# _*_ coding:utf-8 _*_
import numpy as np
import requests
import json
import urllib.parse
import random

header = {
    # ':authority': 'www.xiami.com',
    # ':method': 'GET',
    # ':path': '/song/playlist/id/1801743401/object_name/default/object_id/0/cat/json?_ksTS=1540223562802_929&callback=jsonp930',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'gid=154021559657442; PHPSESSID=81ddcaf4a68b1155840d42c585e0b693; _xiamitoken=6897bee0b281b54ab93790f6171910ba; _unsign_token=2692d83f48ae63d5ce368df9db20fce1; UM_distinctid=1669c00e828183-04c433c290ca4-172a1c0b-1fa400-1669c00e829f9e; cna=HrdQFMCSYkICAWovEVjAhk/a; join_from=0T2dTo8YuGA12%2F%2FB; xmgid=ddad09f9-04e8-4cf7-8147-4e7be563e51d; __XIAMI_SESSID=4b5d97b3bf516c9d6fdd00e115febbe2; _umdata=0823A424438F76AB77E6C117C27FE9E0701310572FA32EA30248E580321AE0807EC1CC65605A4EFDCD43AD3E795C914C65D3F3E94F69106949A2C2F88C1B4986; CNZZDATA2629111=cnzz_eid%3D815441825-1540215292-%26ntime%3D1540226098; CNZZDATA921634=cnzz_eid%3D1061709099-1540215592-%26ntime%3D1540226393; __guestplay=MTc5Njg5NDk5MSwyOzE3NzUwMTg4MjAsODsxNzk1OTY5MTEwLDI7MTgwNDgyOTAxMiwyOzE4MDE3NDM0MDEsOTsxODAxNTEyODcyLDI7MjExMDM0OCw1OzE3NzQ3NDcxMjYsMQ%3D%3D; XMPLAYER_isOpen=1; XMPLAYER_url=/song/playlist/id/1775018820/object_name/default/object_id/0; XMPLAYER_addSongsToggler=1; xm_token=640a2baf8b3261b339aaa3e40a5daae1; uidXM=406622536; member_auth=hmueEtlCuTpkhKGeRI03JyIX57fSSDnVxttTj%2BUr5QcmLdtYYNCvmquVQg1O2iKWq14mzA4NCKXIyUbjO6P1lPTC; isg=BImJ5nwvNvZSrcoBSIFfDOPjmLzp_6C8nBXY1iv_QHCvcqGEYiTn2aDjsJbhKhVA; user=406622536%22%E8%83%A1%E5%AE%B6%E6%98%8E+Jemmy%22images%2Favatar_new%2F1489646172_1540228492.jpg%220%220%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv1%3C%2Fa%3E%220%220%220%222d0a4acade%221540228568; t_sign_auth=0',
    'referer': 'https://www.xiami.com/play?ids=/song/playlist/id/2110348/object_name/default/object_id/0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


class Xiami(object):
    def __init__(self, url):
        self.proxy_list = requests.get("http://localhost:8899/api/v1/proxies").json()
        self.path = '/home/hujiaming/Music/'  # 本地存储路径（后面带"/"）
        self.url = url

    def run(self):
        location = self._get_location()
        matrix = self._from_location_to_url(location)
        url = self._from_matrix_to_url(matrix)
        print("是否下载", self.name, "?")
        try:
            tag = int(input("是 请输入1，否 输入0:"))
        except Exception as e:
            return
        if tag == 1:
            self.download(url)

    def _get_location(self):
        random_proxy = random.choice(self.proxy_list['proxies'])
        res = requests.get(self.url, headers=header,
                           proxies={'http': 'http://{0}:{1}'.format(random_proxy['ip'], random_proxy['port'])})
        data = json.loads(res.text[(res.text.find("(") + 1):-1])
        # print(data)
        location = data['data']['trackList'][0]['location']
        self.name = data['data']['trackList'][0]['name']
        # print(location)
        # print(len(location) - 1)
        return location

    def _from_location_to_url(self, location):
        num = int(location[0])
        # print(num)
        location_new = location[1:]
        l = 1
        if int(len(location_new) / num) == len(location_new) / num:
            step = int(len(location_new) / num)
            normal_num = num
            # print('normal')
        else:
            # print('abnormal')
            step = int(len(location_new) / num) + 1
            normal_num = num - (step * num - len(location_new))
            # print(step, normal_num)
            # TODO: 如果缺少，那么后面几行各空一位，那么少一位的行总数为：(num - len(location_new) % num)
        matrix = []
        for i in range(num):
            s = []
            if i < normal_num:
                # print(step * i, step * (i + 1))
                for j in range(step * i, step * (i + 1)):
                    s.append(location_new[j])
                j += 1
            else:
                # print(j, step * (i + 1) - l)
                for k in range(j, step * (i + 1) - l):
                    s.append(location_new[k])
                s.append("#")
                j = k + 1
                l += 1
            # print(s)
            # print(len(s))
            matrix.append(s)
        return matrix

    def _from_matrix_to_url(self, matrix):
        # print(matrix)
        tem = np.array(matrix)
        url = ''
        for i in range(len(matrix[0])):
            tmp = "".join(tem[:, i])
            tmp = "".join([k for k in tmp if k != "#"])
            url += tmp
        # print(url)
        url = "https:" + urllib.parse.unquote(url).replace("^", '0')
        # print(url)
        return url

    def download(self, url):
        random_proxy = random.choice(self.proxy_list['proxies'])
        with open(self.path + self.name + ".mp3", 'wb') as f:
            f.write(requests.get(url, headers=header, proxies={
                'http': 'http://{0}:{1}'.format(random_proxy['ip'], random_proxy['port'])}).content)
        print(self.name + "下载完成")


if __name__ == '__main__':
    # TODO: 使用scylla抓以下代理IP，然后去搞，解除封禁IP的风险
    xiami = Xiami(
        'https://www.xiami.com/song/playlist/id/1806304949/object_name/default/object_id/0/cat/json?_ksTS=1540236428450_2563&callback=jsonp2564')
    xiami.run()

# 以下代码为分析凯撒矩阵使用
# https%3a %2f%2f m128.xiami.net %2f 892 %2f 2110467892 %2f 2103784157 %2f 1805599073_1539243969099.mp3 %3f auth_key %3d 1540868400-0-0-b69ffbbaf4ec466df9408c3297baae78
# ['%', 'm', 'i', 'e', '9', '1', '6', '2', 'E', '5', '8', '9', '3', '2', '%', 'm', 'a', 'e', '5', '6', '%', 'E', 'b', 'b', '4', '4', '3', 'a']
# ['2', '1', 'a', 't', '2', '1', '7', 'F', '3', '7', '%', '9', '_', '4', '5', 'p', 'u', 'y', '4', '8', '5', '-', '6', 'a', '6', '%', '2', 'e']
# ['F', '2', 'm', '%', '%', '%', '8', '2', '7', '%', '5', '%', '1', '3', 'E', '3', 't', '%', '%', '4', 'E', '%', '9', 'f', '6', '5', '9', '7']
# ['%', '8', 'i', '2', '2', '5', '9', '1', '8', '2', 'E', '5', '5', '9', '9', '%', 'h', '3', '5', '%', '-', '5', 'f', '4', 'd', 'E', '7', '8']
# ['2', '.', '.', 'F', 'F', 'E', '2', '%', '4', 'F', '5', 'E', '3', '6', '9', '3', '_', 'D', 'E', '5', '%', 'E', 'f', 'e', 'f', '8', 'b', 'F']
# ['x', 'n', '8', '2', '4', '%', '5', '1', '1', '5', '7', '9', '9', '.', 'F', 'k', '1', '8', 'E', '5', '-', 'b', 'c', '9', 'c', 'a', ' ', ' ']
# 6%mie9162E58932%mae56%Ebb443a21at217F37%9_45puy485-6a6%2eF2m%%%827%5%13E3t%%4E%9f6597%8i2259182E5599%h35%-5f4dE78 2..FFE2%4F5E3693_DE5%Efef8bF xn824%5115799.Fk18E5-bc9ca
# %mie9162E58932%mae56%Ebb443a
# 21at217F37%9_45puy485-6a6%2e
# F2m%%%827%5%13E3t%%4E%9f6597
# %8i2259182E5599%h35%-5f4dE78
# 2..FFE2%4F5E3693_DE5%Efef8b
# Fxn824%5115799.Fk18E5-bc9ca
