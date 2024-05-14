# inheritance

class Animal:
    def eating(self):
        print("냥냥념념뇽뇽")

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("냐옹")



a = Dog()
a.eating()
a.speak()

b = Cat()
b.eating()
b.speak()









