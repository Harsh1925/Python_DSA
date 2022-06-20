class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius ** 2 * Circle.pi

    def get_circumference(self):
        return self.radius * 2 * self.pi


new_circle = Circle(30)
print(new_circle.get_circumference())
print(new_circle.area)
