import random

class MapGenerator(object):
    def __init__(self):
        self.w = 30
        self.h = 20
        self.map_info = [[0 for x in range(self.w)] for y in range(self.h)]
    
    def EmptyMap(self):
        return self.map_info
    
    def LoadMap(self, file_name):
        f = open(file_name, 'r')
        lines = f.readlines()
        for j in range(self.h):
            bits = lines[j].split()
            for i in range(self.w):
                self.map_info[j][i] = int(bits[i])
        return self.map_info
