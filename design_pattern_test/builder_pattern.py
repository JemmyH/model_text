# _*_ coding:utf-8_*_
from abc import ABCMeta,abstractmethod

# 产品
class Player(object):
    def __init__(self,face=None,body=None,arm=None,leg=None):
        self.face = face
        self.body = body
        self.arm =arm
        self.leg = leg
    def __str__(self):
        return "{} {} {} {}".format(self.face,self.body,self.arm,self.leg)

# 建造者
class Builder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass

# 具体建造者
class BuildWoman(Builder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = '圆脸蛋'
    def build_body(self):
        self.player.body = '好身材'
    def build_arm(self):
        self.player.arm = '瘦胳膊'
    def build_leg(self):
        self.player.leg = '大长腿'
    def get_player(self):
        return self.player

# 指挥者 
class PlayerDirector(object):
    def build_player(self,specific_builder):
        specific_builder.build_face()
        specific_builder.build_body()
        specific_builder.build_arm()
        specific_builder.build_leg()
        return specific_builder.get_player()

if __name__ == '__main__':
    director = PlayerDirector()
    specific_builder = BuildWoman()
    print("建造了一个女人：")
    p = director.build_player(specific_builder)
    print(p)
