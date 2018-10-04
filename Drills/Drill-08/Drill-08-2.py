from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
size = 10

direction = 0
frame = 0
x, y = 0, 0


def print_stamp():
    pass


def add_stamp(p):
    global stamp
    stamp = stamp + (p, direction)


def animation_character():
    if direction == 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)


def draw_all():
    global frame
    animation_character()
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    animation_character()
    print_stamp()
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.05)
    pass


def smooth_move(random_list):
    global x, y
    loop = -1
    while True:
        p1 = random_list[loop]
        p2 = random_list[loop + 1]
        p3 = random_list[loop + 2]
        p4 = random_list[loop + 3]
        for i in range(0, 100, 2):
            t = i / 100
            x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
            y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2

        x, y = p3
        add_stamp(p3)
        loop = (loop + 1) % size
    pass


def move_to(p1, p2):
    global x, y
    global frame
    global direction
    x, y = p1
    if p1[0] - p2[0] > 0:
        direction = 0
    else:
        direction = 1
    for i in range(1, 100, 10):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        animation_character(direction)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.05)
    x, y = p2
    pass





random_move_list = [(random.randint(100, 1000), random.randint(100, 800)) for n in range(size)]
stamp = [(random_move_list[0], 0)]
x, y = random_move_list[0]
while True:
    smooth_move(random_move_list)
    print_stamp()





