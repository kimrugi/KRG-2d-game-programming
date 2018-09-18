from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')
speed = 5


def animation_character(theta):
    if -90 < theta < 90:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)


def calculate_degree(to_x, to_y):
    return math.atan2(to_y - y, to_x - x)


def move_to(to_x, to_y):
    global x
    global y
    global frame
    theta = calculate_degree(to_x, to_y)
    degree = math.degrees(theta)
    sin = math.sin(theta)
    cos = math.cos(theta)
    print(degree)
    print(sin)
    print(cos)
    while not (x - 5 < to_x < x + 5) and not (y - 5 < to_y < y + 5):
        clear_canvas()
        grass.draw(400, 30)
        animation_character(theta)
        frame = (frame + 1) % 8
        update_canvas()
        x = x + speed * math.cos(theta)
        y = y + speed * math.sin(theta)
        delay(0.05)


while True:
    frame = 0
    x, y = 712, 349
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
