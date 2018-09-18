from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

LEFT_UP = 0
LEFT_DOWN = 1
RIGHT_UP = 2
RIGHT_DOWN = 3

x, y = 203, 535
speed = 1


def calculate_degree(to_x, to_y):
    pass



def move_to(to_x, to_y):
    while to_x != x or to_y != y:
        theta = calculate_degree(to_x, to_y)
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
