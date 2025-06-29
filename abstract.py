from abc import ABC, abstractmethod

class hello(ABC):
    def print(self, a):
        print("Passed value is", a)
    @abstractmethod
    def test(self):
        print("This is inside hello class.")

class testclass(hello):
    def test(self):
        print("This inside test class.")

obj1=testclass()
obj1.test()
obj1.print(200)