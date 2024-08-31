from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def printInfo(self):
        pass
class Case1(Test):
    def __init__(self):
        self.name = "Thevmini"
    def printInfo(self):
        return self.name
    
test1 = Case1()
print(test1.printInfo())