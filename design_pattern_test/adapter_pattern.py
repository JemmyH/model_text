# _*_ coding:utf-8 _*_

# 在原来的旧系统中，有以下两个类
class Synthesizer(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    def play(self):
        return "is playing a song"
class Human(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "the {} human".format(self.name)
    def speak(self):
        return "is saying hello"

# 现在新增一个类
class Computer(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "the {} computer".format(self.name)
    def execute(self):
        return "is executing an program"
"""
对于扩展系统来说，所有动作函数均使用 Obj.execute() 来执行。即对于调用者来说，原系统的 Synthesizer.play() 和 Human.speak() 是不存在的，必须像调用 Computer.execute() 一样使用 Synthesizer.execute() 和 Human.execute() 来调用原系统中对象的执行函数。
这就是我们之前提到的场景，无法修改原系统函数，此时新系统就可以采用适配器模式进行设计。
"""

# 新建一个类专门用于统一接口
class Adapter(object):
    def __init__(self,obj,adapted_method):
        self.obj = obj
        self.__dict__.update(adapted_method)
        # 这里是使用了 Python 的一个特殊语法糖 class.__dict__ 属性，即类的内部字典。这个特殊的属性是一个字典，存放了这个类所包含的所有属性，包括方法。所以这里将传入的类进行处理，将需要被适配器处理的方法添加到内部字典中，生成一个属于这个新适配器对象的方法。
    def __str__(self):
        return str(self.obj)

if __name__ == '__main__':
    objects = [Computer('Lenovo')]
    synth = Synthesizer('Guita')
    objects.append(Adapter(synth,dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human,dict(execute=human.speak)))

    for i in objects:
        print("{} {}".format(str(i),i.execute()))
