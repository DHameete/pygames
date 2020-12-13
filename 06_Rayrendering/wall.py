from pygame import math, draw

class Wall:

    def __init__(self, p1, p2, color):
        self.a = math.Vector2(p1)
        self.b = math.Vector2(p2)
        self.color = color

    def show(self, surface):
        draw.aaline(surface, self.color, self.a/4+(1,1), self.b/4+(1,1), 1)
