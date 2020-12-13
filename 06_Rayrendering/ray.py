from pygame import math, draw

class Ray:

    def __init__(self, pos, angle, color):
        self.pos = pos
        self.dir = math.Vector2(1, 0)
        self.initangle = angle
        self.angle = 0
        self.dir = self.dir.rotate(angle)
        self.color = color

    def lookAt(self, x, y):
        self.dir.x = x - self.pos.x
        self.dir.y = y - self.pos.y
        self.dir.normalize()

    def show(self, surface):
        end = self.pos/4 + 30 * self.dir
        draw.aaline(surface, self.color, self.pos/4, end, 1)

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if(den == 0):
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (t > 0 and t < 1 and u > 0):
            pt = wall.a + t * (wall.b - wall.a)
            return pt
        else:
            return

    def rotate(self, angle):
        delta_angle = self.angle - angle
        if delta_angle != 0:
            self.dir = self.dir.rotate(delta_angle)
            self.angle = angle
