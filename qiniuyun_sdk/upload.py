# _*_ coding:utf-8 _*_
from qiniu import Auth
from qiniu import BucketManager

# 需要填写你的 Access Key 和 Secret Key
access_key = 'your access key'
secret_key = 'your secret key'
# 构建鉴权对象
bucket_name = 'xgyw'
q = Auth(access_key, secret_key)
# 要上传的空间
bucket = BucketManager(q)

def upload(url,file_name):
    ret, info = bucket.fetch(url, bucket_name, file_name)
    print(info)
    assert ret['key'] == file_name
    
if __name__ == '__main__':
    upload("your url","your file_name")