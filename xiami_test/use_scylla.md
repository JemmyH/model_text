### 1. 免费IP代理工具——scylla
#### 1.1 配置环境
```bash
# 首先建立虚拟环境
virtualenv scylla_env
source scylla_env/bin/activate
# 然后安装python3.6开发环境
pip install --upgrade pip  # 先升级pip至最新
pip install python3.6-dev(如果这一步不成功请跳过，并且在后面使用pip3)
# 下一步安装scylla
pip install scylla
# 启动scylls
scylla  # 此时可以点击提示中的链接或者在浏览器直接打开‘http://0.0.0.0:8899/’来查看已获取的ip地址(刚开始会有点慢)
```
#### 1.2 requests实操
```python
# 现在shell命令行中启动scylla：scylla
# 此时你可以打开http://127.0.0.1:8899 去查看已经获取到的代理IP
import requests
import random
proxies_list = requests.get('http://localhost:8899/api/v1/proxies').json()  # 获取所有的IP
ran_proxy = random.choice(proxies_list['proxies'])  # 从中选取一个IP
res = requests.get('your/want_to/request/url',proxies={'http':'http://{0}:{1}'.format(ran_proxy['ip'],ran_proxy['port'])})
print(res.text)
```