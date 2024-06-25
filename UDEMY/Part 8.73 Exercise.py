from math import sqrt
class Line():
    def __init__(self, coor1, coor2) -> None:
        self.coor1 = coor1
        self.coor2 = coor2
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
    def distance(self):
        return sqrt((self.coor2[1]-self.coor1[1])**2 + (self.coor2[0]-self.coor1[0])**2)
    
coordinate1 =(3,2)
coordinate2 =(8,10)
li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())

class Cylinder():
    pi = 3.14
    def __init__(self, height=1, radius=1) -> None:
        self.height = height
        self.radius = radius
    def volume(self):
        return self.height * Cylinder.pi * (self.radius ** 2)
    def surface_area(self):
        return self.height * 2 * Cylinder.pi * self.radius + Cylinder.pi * (self.radius ** 2) *2
    
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
    