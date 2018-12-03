# _*_ coding:utf-8 _*_
from abc import ABCMeta, abstractmethod


# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# 抽象工厂


class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# 具体产品


class MiShell(PhoneShell):
    def show_shell(self):
        print("小米手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class DragonCpu(CPU):
    def show_cpu(self):
        print('晓龙CPU')


class QilinCpu(CPU):
    def show_cpu(self):
        print('麒麟CPU')


class AppleCpu(CPU):
    def show_cpu(self):
        print('苹果CPU')


class Android(OS):
    def show_os(self):
        print('Android系统')


class IOS(OS):
    def show_os(self):
        print('IOS系统')

# 具体的工厂


class MiFactory(PhoneFactory):
    def make_shell(self):
        return MiShell()

    def make_cpu(self):
        return DragonCpu()

    def make_os(self):
        return Android()


class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_cpu(self):
        return QilinCpu()

    def make_os(self):
        return Android()


class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCpu()

    def make_os(self):
        return IOS()

# 客户端


class Phone(object):
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print("生产手机信息：")
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()


def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)


if __name__ == '__main__':
    p1 = make_phone(AppleFactory())
    p1.show_info()
