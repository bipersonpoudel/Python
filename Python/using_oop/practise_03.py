class Circle:
    def __init__(self, radius):
        self.radius=radius
    def Area(self):
        area=3.14*self.radius*self.radius
        print("Area is: ",area)

    def perimeter(self):
        peri=2*3.14*self.radius
        print("Perimeter is: ",peri)


c1=Circle(14)
c1.Area()
c1.perimeter()