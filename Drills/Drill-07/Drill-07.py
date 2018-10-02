from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
size = 20

def move_to(p1, p2):
    pass

def animation_character(theta):

        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    pass

random_move_list = [(random.randint(100, 1000), random.randint(100, 800)) for n in range(size)]
roop = 1
while True:
    move_to(random_move_list[roop - 1], random_move_list[roop])
    clear_canvas()
    kpu_ground.draw(400, 30)
    animation_character(theta)
    frame = (frame + 1) % 8
    update_canvas()
    x = x + speed * math.cos(theta)
    y = y + speed * math.sin(theta)
    delay(0.05)
    roop = (roop + 1) % size




