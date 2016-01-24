import turtle
import math

class Polygon:
    def __init__(self):
        assert type(self) != Polygon, "Polygon class should not be instantiated!"

    def get_points(self):
        raise NotImplementedError("You must implement a get_points method for your %s class!" % str(type(self).__name__))

    def draw(self):
        points = self.get_points()
        turtle.speed(2) # draw a little faster...

        turtle.clear()
        turtle.penup()

        if len(points) > 0:
            start = points.pop(0)
        else:
            start = (0, 0)

        turtle.setposition(start)
        points.append(start) # be sure we connect the ends

        turtle.pendown()
        for point in points:
            d = turtle.distance(point)
            h = turtle.towards(point)
            turtle.setheading(h)
            turtle.forward(d)

        turtle.hideturtle()
        turtle.exitonclick()

def find_point(pos, a, d):
    s = math.sin(math.radians(a))
    c = math.cos(math.radians(a))

    x0 = pos[0]
    y0 = pos[1]

    x1 = x0 + (d * c)
    y1 = y0 + (d * s)
    return (round(x1, 2), round(y1, 2))
