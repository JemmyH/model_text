# _*_ coding:utf-8_*_
from abc import ABCMeta, abstractmethod


class Pay(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Pay):
    def pay(self, money):
        print("使用支付宝支付{}元".format(money))


class WechatPay(Pay):
    def pay(self, money):
        print("使用微信支付了{}元".format(money))


class FactoryPattern(object):
    def use_payment(self, way):
        if way == 'alipay':
            return AliPay()  # 返回对象实例
        elif way == 'wechat':
            return WechatPay()


if __name__ == '__main__':
    p = FactoryPattern()
    m = p.use_payment('alipay')
    m.pay(100)
