from coordinate import Coordinate

class Path():
    def __init__(self, coord_, coord_list_):
        self.coord = coord_
        self.coord_list = coord_list_

class Planner():
    def __init__(self, start_coord, end_coord, map_info):
        self.visited = set([])
        self.sucessors = [Path(start_coord, [start_coord])]
        self.start = start_coord
        self.end = end_coord
        self.map_info = map_info

    def GetVisited(self):
        return self.visited

    def GetSuccessors(self):
        successor_coords = [i.coord for i in self.sucessors]
        return successor_coords

    def GetSuccessorsForCoord(self, coord_path):
        neighbors = coord_path.coord.GetNeighbors()
        real_successors = []
        for n in neighbors:
            if self.map_info[n.x][n.y] == 0:
                tmp_list = list(coord_path.coord_list)
                tmp_list.append(n)
                real_successors.append(Path(n, tmp_list))
        return real_successors
    
    # Check empty before use
    def GetNextCoord(self):
        next_coord_path = self.sucessors[0]
        self.sucessors = self.sucessors[1:]
        return next_coord_path

    def PutNextCoord(self, next_coord_path):
        self.sucessors.append(next_coord_path)

    # Return: completed, succeed, path
    def Step(self):
        if len(self.sucessors) == 0:
            return True, False, Path(self.start, [self.start])
        else:
            next_coord_path = self.GetNextCoord()
            self.visited.add(next_coord_path.coord)
            if next_coord_path.coord == self.end:
                return True, True, next_coord_path
            else:
                coord_path_successors = self.GetSuccessorsForCoord(next_coord_path)
                for coord_path_successor in coord_path_successors:
                    self.PutNextCoord(coord_path_successor)
                return False, False, Path(self.start, [self.start])
