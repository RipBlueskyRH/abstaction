from abc import ABC

class Animal(ABC):
    def test(self):
        pass

class Human(Animal):
    def test(self):
        print("I can run")

class Snake(Animal):
    def test(self):
        print("I can slither")

class Cat(Animal):
    def test(self):
        print("I can climb trees")

class Dog(Animal):
    def test(self):
        print("I can bark")

a=Human()
a.test()
b=Snake()
b.test()
c=Cat()
c.test()
d=Dog()
d.test()