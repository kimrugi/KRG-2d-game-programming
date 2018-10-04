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
def smooth_move(random_list)
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


def animation_character(direction):
    if direction == 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)


random_move_list = [(random.randint(100, 1000), random.randint(100, 800)) for n in range(size)]
stamp = [random_move_list[0]]

while True:
    smooth_move(random_move_list)
    print_stamp()





