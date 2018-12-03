# _*_ coding:utf-8 _*_

from abc import ABCMeta,abstractmethod

# 抽象实体基类
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

# 实体
class RealSubject(Subject):
    def __init__(self,filename):
        print("正在读取{}文件内容".format(filename))
        with open('filename') as f:
            self.content = f.read()
    def get_content(self):
        return self.content

# 远程代理
class ProxyRemote(Subject):
    def __init__(self,filename):
        self.sub = RealSubject(filename)
    def get_content(self):
        return self.sub.get_content()

# 虚代理
class ProxyVirtual(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.sub = None
    def get_content(self):
        if not self.sub:
            self.sub = RealSubject(self.filename)
        return self.sub.get_content()

# 保护代理
class ProxyProtect(Subject):
    def __init__(self,filename):
        self.sub = RealSubject(filename)
    def get_content(self):
        # ...
        # 进行一些逻辑操作、添加一些功能，比如验证操作，保护文件内容
        return "???"

if __name__ == '__main__':
    filename = 'test.txt'
    username = input("请输入用户名")
    if username == 'root':
        p = ProxyRemote(filename)
    elif username == 'user1':
        p = ProxyVirtual(filename)
    else:
        p = ProxyProtect(filename)
    print(p.get_content())