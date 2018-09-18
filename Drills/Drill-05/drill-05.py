from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def animation_character(frame, theta):
    if theta > 90 or theta < 270 :
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8


def calculate_degree(x, y, to_x, to_y):
    return math.atan2(to_y - y, to_x - x)


def move_to(x, y, to_x, to_y, frame):
    speed = 1
    theta = calculate_degree(x, y, to_x, to_y)
    while to_x != x or to_y != y:
        clear_canvas()
        grass.draw(400, 30)
        animation_character(frame, theta)
        update_canvas()
        x = x + speed * math.sin(theta)
        y = y + speed * math.cos(theta)
        delay(0.01)



while True:
    frame = 0
    x, y = 711.0, 349.0
    move_to(x, y, 203, 535, frame)
    move_to(x, y, 132, 243, frame)
    move_to(x, y, 535, 470, frame)
    move_to(x, y, 477, 203, frame)
    move_to(x, y, 715, 136, frame)
    move_to(x, y, 316, 225, frame)
    move_to(x, y, 510, 92, frame)
    move_to(x, y, 692, 518, frame)
    move_to(x, y, 682, 336, frame)
    move_to(x, y, 712, 349, frame)

close_canvas()
