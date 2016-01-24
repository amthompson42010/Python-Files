from polygon import Polygon, find_point

class Example(Polygon):
    def __init__(self, angle):
        super().__init__()
        self._angle = angle

    def get_points(self):
        start = (100, 100)
        points = [start]

        next_point = find_point(start, self._angle, 100)
        points.append(next_point)

        next_point = find_point(next_point, 1.5 * self._angle, 150)
        points.append(next_point)

        points.append((-100, -100))
        points.append((0, 100))

        return points

class Rectangle(Polygon):
    def __init__(self, shortside, longside):
        super().__init__()
        self._shortside = shortside
        self._longside = longside

    def get_points(self):
    
        start = (50, 50)
        points = [start]

        next_point = find_point(start, 0, self._shortside)
        points.append(next_point)

        next_point = find_point(next_point, 90, self._longside)
        points.append(next_point)

        next_point = find_point(next_point, 180, self._shortside)
        points.append(next_point)

        next_point = find_point(next_point, 270, self._longside)
        points.append(next_point)

        return points

class Square(Rectangle):

    def __init__(self, sidelength):
        self._sidelength = sidelength
        super().__init__(sidelength, sidelength)
"""
    def get_points(self):
        start = (50, 50)
        points = [start]

        next_point = find_point(start, 0, self._sidelength)
        points.append(next_point)

        next_point = find_point(next_point, 90, self._sidelength)
        points.append(next_point)

        next_point = find_point(next_point, 180, self._sidelength)
        points.append(next_point)

        next_point = find_point(next_point, 270, self._sidelength)
        points.append(next_point)

        return points
"""
class Triangle(Polygon):
    def __init__(self, side1, side2, degree):
        super().__init__()
        self._side1 = side1
        self._side2 = side2
        self._degree = degree

    def get_points(self):
        start = (50, 50)
        points = [start]

        next_point = find_point(start, 0, self._side1)
        points.append(next_point)

        next_point = find_point(next_point, 180 - self._degree, self._side2)
        points.append(next_point)

        return points

class EquilateralTriangle(Polygon):
    def __init__(self, length):
        self._length = length
    
    def get_points(self):
        start = (50, 50)
        points = [start]

        next_point = find_point(start, 0, self._length)
        points.append(next_point)

        next_point = find_point(next_point, 120, self._length)
        points.append(next_point)

        return points

def main():
 
    a = Example(101)
    a.draw()

    b = Example(201)
    b.draw()

    c = Rectangle(100, 70)
    c.draw()

    d = Square(100)
    d.draw()

    e = EquilateralTriangle(100)
    e.draw()

    f = Triangle(100, 100, 270)
    f.draw()


if __name__ == '__main__':
    main()
