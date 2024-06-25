#ke thua
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
    def who_am_i(self):
        print("I am a Dog")
    def bark(self):
        print ("WOOF!")
mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()
#da hinh
class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + "says woof!"
class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + "says meow!"

niko = Dog('niko')
felix = Cat('felix')

def animal_speak(animal):
    print(animal.speak())

animal_speak(niko)
animal_speak(felix)

#lop truu tuong -> chi duc thiet ke la lop co so de ke thua
class DongVat():
    def __init__(self,name) -> None:
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
dongvat = DongVat('hehe')
dongvat.speak()