from settings import *
from spot import Spot

class Grid:

    def __init__(self, cols, rows):
        self.cols = cols # temp
        self.rows = rows # temp
        w = WIDTH / cols
        h = HEIGHT / rows
        self.spots = [[Spot(r,c,w,h) for c in range(cols)] for r in range(rows)]

    def show(self,surface):
        for spot_row in self.spots:
            for spot in spot_row:
                spot.show(surface)


    def checkNeighbor(self):
    # print(grid.spots[row][col])
        for spot_row in self.spots:
            for spot in spot_row:
                r = spot.r
                c = spot.c
                if(r > 0):
                    spot.addNeighbors(self.spots[r-1][c])
                    # print("UP")
                if(r < self.rows - 1):
                    spot.addNeighbors(self.spots[r+1][c])
                    # print("DOWN")
                if(c > 0):
                    spot.addNeighbors(self.spots[r][c-1])
                    # print("LEFT")
                if(c < self.cols - 1):
                    spot.addNeighbors(self.spots[r][c+1])
                    # print("RIGHT")