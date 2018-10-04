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
    for st in stamp:
        if st[1] == 0:
            character.clip_draw(st[2] * 100, 0, 100, 100, st[0][0], st[0][1])
        else:
            character.clip_draw(st[2] * 100, 100, 100, 100, st[0][0], st[0][1])
    pass


def add_stamp(p):
    global stamp
    tmp = (p, direction, frame)
    stamp.append(tmp)


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
    get_events()
    delay(0.05)
    pass


def smooth_move(random_list):
    global x, y
    global direction
    loop = 2
    while True:
        p4 = random_list[loop]
        p3 = random_list[loop - 1]
        p2 = random_list[loop - 2]
        p1 = random_list[loop - 3]
        for i in range(0, 100, 5):
            t = i / 100
            tmpx = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
            y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
            if(x < tmpx):
                direction = 1
            else:
                direction = 0
            x = tmpx
            draw_all()

        x, y = p3
        add_stamp(p3)
        loop = (loop + 1) % size
    pass


random_move_list = [(random.randint(100, 1000), random.randint(100, 800)) for n in range(size)]
stamp = [(random_move_list[0], 0, 0)]
x, y = random_move_list[0]


smooth_move(random_move_list)





