class circle():

    pi = 3.14

    def __init__(self, radius):

        self.radius = radius

    def get_circumference(self):

        return self.radius* 2 * self.pi


new_circle = circle(30)
print(new_circle.get_circumference)