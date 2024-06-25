class NameOfClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    def some_method(self):
        print(self.param1)

class Dog():
    #Class object attribute
    #same for any instance of class
    tiengsua = 'Gau gau'
    def __init__(self,tencho,loai,codom) -> None:
        #Thuoc tinh
        self.ten = tencho
        self.loai = loai
        self.codom = codom
    #operation/actions -> method
    def bark(self,number):
        print('WOOF ! {} {}'.format(self.ten, number))

mydog = Dog( 'Lab', 'Huskie', True)
mydog1 = Dog(tencho= 'Lab',loai= 'Huskie',codom= True)
print(type(mydog))
print(mydog.ten)
print(mydog.tiengsua)

mydog.bark(1)

class Circle():
    #class object attribute
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius*radius* Circle.pi
    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
my_circle = Circle()
print(my_circle.get_circumference())
print(my_circle.area)
