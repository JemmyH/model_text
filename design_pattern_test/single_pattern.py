# _*_ coding:utf-8 _*_
class SingalPattern(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingalPattern, cls).__new__(cls)
        return cls._instance


class MySingal(SingalPattern):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = MySingal('a')
    b = MySingal('b')
    print(a)
    print(b)
    print(a.name)
    print(b.name)
    a.name = 'changed'
    print(a.name)
    print(b.name)
