from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        return "Humans can walk and run."

class Dog(Animal):
    def move(self):
        return "Dogs can walk and run on four legs."

human = Human()
dog = Dog()

print(human.move())
print(dog.move())