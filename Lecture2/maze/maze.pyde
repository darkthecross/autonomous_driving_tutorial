from map_generator import MapGenerator
from coordinate import Coordinate
from planner import Planner

# global config
grid_size = 10
grid_border = 1
empty_color = color(220, 220, 220)
block_color = color(70, 70, 70)
visited_color = color(0, 150, 0)
successor_color = color(0, 220, 0)
path_color = color(220, 220, 0)
edit_mode = False
planning_ended = False
repeat_step = False

inner_map = MapGenerator()
map_height = 20
map_width = 30
map_info = inner_map.EmptyMap()
# map_info = inner_map.LoadMap('map_simple.txt')
# map_info = inner_map.LoadMap('map_barriers.txt')
map_info = inner_map.LoadMap('map_blocked.txt')

p = Planner(Coordinate(0, 0), Coordinate(44, 59), map_info)

def draw_grid(i, j):
    rect((grid_size+grid_border)*j+grid_border, (grid_size+grid_border)*i+grid_border, grid_size, grid_size)

def setup():
    size((grid_size+grid_border)*map_width+grid_border, (grid_size+grid_border)*map_height+grid_border, P2D)
    noStroke()
    background(0)
    
def step_planning():
    global planning_ended
    if planning_ended:
        return
    visited = p.GetVisited()
    for v in visited:
        map_info[v.x][v.y] = 2
    successors = p.GetSuccessors()
    for s in successors:
        map_info[s.x][s.y] = 3
    ended, succeed, path = p.Step()
    if ended:
        planning_ended = True
        if succeed:
            for v in path.coord_list:
                map_info[v.x][v.y] = 4
    else:
        return

def draw():
    for i in range(map_height):
        for j in range(map_width):
            if map_info[i][j] == 1:
                fill(block_color)
            elif map_info[i][j] == 0:
                fill(empty_color)
            elif map_info[i][j] == 2:
                fill(visited_color)
            elif map_info[i][j] == 3:
                fill(successor_color)
            elif map_info[i][j] == 4:
                fill(path_color)
            draw_grid(i, j)
    if repeat_step:
        step_planning()

def keyPressed():
    if key == 'c':
        for i in range(map_height):
            for j in range(map_width):
                map_info[i][j] = 0
    if key == 's':
        f = open("test.txt",'w')
        for i in range(map_height):
            s = ''
            for j in range(map_width):
                s += str(map_info[i][j])
                if not j == map_width-1:
                    s += ' '
            s += '\n'
            f.write(s)
    if key == 'e':
        global edit_mode
        edit_mode = ~edit_mode
    if key == ' ':
        global repeat_step
        repeat_step = True

def keyReleased():
    if key == ' ':
        global repeat_step
        repeat_step = False
                

def mouseDragged():
    if edit_mode:
        j = mouseX/(grid_size+grid_border)
        i = mouseY/(grid_size+grid_border)
        map_info[i][j] = 1
    
