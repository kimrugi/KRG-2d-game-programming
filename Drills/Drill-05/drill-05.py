from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

LEFT = 0
RIGHT = 1

x, y = 203, 535
speed = 1
frame = 0

def animation_character():
    pass

import math
def calculate_degree(to_x, to_y):
    return math.atan((to_y - y) / (to_x - x))

def move_to(to_x, to_y):
    theta = calculate_degree(to_x, to_y)
    while to_x != x or to_y != y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = x + speed * math.sin(theta)
        y = y + speed * math.cos(theta)
        animation_character()
        delay(0.01)
    pass

while True:
    move_to(203, 535)
    move_to(132, 243)
    move_to(535, 470)
    move_to(477, 203)
    move_to(715, 136)
    move_to(316, 225)
    move_to(510, 92)
    move_to(692, 518)
    move_to(682, 336)
    move_to(712, 349)

close_canvas()
