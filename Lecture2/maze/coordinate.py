class Coordinate(object):
    def __init__(self, xx = 0, yy = 0, hh = 0):
        self.x = xx
        self.y = yy
        self.h = hh
        self.x_min = 0
        self.x_max = 19
        self.y_min = 0
        self.y_max = 29

    def GetNeighbors(self):
        neighbors = []
        if self.x > self.x_min:
            neighbors.append(Coordinate(self.x-1, self.y, 0))
        if self.y > self.y_min:
            neighbors.append(Coordinate(self.x, self.y-1, 0))
        if self.x < self.x_max:
            neighbors.append(Coordinate(self.x+1, self.y, 0))
        if self.y <self.y_max:
            neighbors.append(Coordinate(self.x, self.y+1, 0))
        return neighbors

    def __str__(self):
        return "[(" + str(self.x) + ", " + str(self.y) + "), h=" + str(self.h)+"]"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
