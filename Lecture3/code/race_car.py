import cv2
from car import Car
import math
import copy
import numpy as np

# draw car in place
def draw_car(img, c, clr):
    return cv2.circle(img,(math.floor(c.y),math.floor(c.x)), 15, clr, 3)

def calc_sensor(map_img, car):
    val = np.ones((5,), np.float32) * -1
    for i in range(5):
        th = car.theta + (i-2)*math.pi/6
        for dist in range(50):
            px = car.x + dist * math.cos(th)
            py = car.y + dist * math.sin(th)
            if int(px) > map_img.shape[0] or int(py) > map_img.shape[1]:
                val[i] = dist
                break
            if map_img[int(px), int(py)] == 255:
                val[i] = dist
                break
        if val[i] == -1:
            val[i] = 50
    return val

def move_car(car, ts, ctl):
    car.x = car.x + math.cos(car.theta) * ts
    car.y = car.y + math.sin(car.theta) * ts
    car.theta = car.theta + ctl

def step(cars):
    for c in cars:
        vals = calc_sensor(binary, c)
        print(vals)
        ctl = 1e-3 * np.dot(vals, c.gene)
        print(ctl)
        move_car(c, 2, ctl)

if __name__ == "__main__":
    # load map
    race_map = cv2.imread('map.png')
    # generate gray image
    gray = cv2.cvtColor(race_map, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("threshold value %s"%ret)

    #c = Car(50.2, 50, 0, np.array([-1, -0.4, 0, 0.4, 1]))

    cars = [Car(50.2, 50, 0, np.array([-1, -0.4, 0, 0.4, 1])), Car(50.2, 50, 0, np.random.rand(5)), Car(50.2, 50, 0, np.random.rand(5))]

    for i in range(1000):
        disp_map = copy.deepcopy(race_map)
        for i in range(3):
            draw_car(disp_map, cars[i], (0, 255 - i * 20, i * 20))
        cv2.imshow("race car", disp_map)
        cv2.waitKey(0)
        step(cars)

