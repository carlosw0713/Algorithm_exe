

class Person:
    gender='男生'

    def __init__(self, name, age):  # 初始化方法
        self.name = name  # 实例化属性
        self.age = age  # 实例化属性

    def say_what(self,say_out):  # 类方法

        print(f"{say_out}, my name is {self.name} and I'm {self.age} years old.")

# 创建实例并传入参数
person1 = Person("John", 25)
person2 = Person("Alice", 30)
person_gender=Person.gender
Person.say_what("你好")

print(person1.name,person2.gender,person_gender)