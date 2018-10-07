# _*_ coding:utf-8_*_

from abc import ABCMeta, abstractmethod


class Pay(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Pay):
    def pay(self, money):
        print("使用支付宝支付{}元".format(money))


class Wechat(Pay):
    def pay(self, money):
        print("使用微信支付{}元".format(money))


class FactoryPattern(metaclass=ABCMeta):
    @abstractmethod
    def use_payment(self):
        pass


class AlipayFactory(FactoryPattern):
    def use_payment(self):
        return AliPay()


class WechatFactory(FactoryPattern):
    def use_payment(self):
        return Wechat()


# 如果要新增支付方式
class ApplePay(Pay):
    def pay(self, money):
        print("使用苹果支付{}元".format(money))

class AppleFactory(FactoryPattern):
    def use_payment(self):
        return ApplePay()


if __name__ == '__main__':
    af = AlipayFactory()
    ali = af.use_payment()
    ali.pay(120)
