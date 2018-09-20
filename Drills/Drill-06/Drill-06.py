from pico2d import *
import math

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
speed = 5
running = 1
frame = 0
is_moving = 0
direction = 1
theta = 0

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
to_x, to_y = x, y
hand_x, hand_y = KPU_WIDTH // 2, KPU_HEIGHT // 2


def calculate_degree():
    global theta
    theta = math.atan2(to_y - y, to_x - x)
    print(theta)


calculate_degree()


def cal_direction():
    global direction
    if -math.pi / 2 < theta < math.pi / 2:
        direction = 1
    else:
        direction = 0


def handle_events():
    global running
    global x, y
    global hand_x, hand_y
    global to_x, to_y
    global is_moving
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            to_x, to_y = hand_x, hand_y
            calculate_degree()
            cal_direction()
            is_moving = 1


def move_to():
    global x, y
    global to_x, to_y
    global is_moving
    x = x + speed * math.cos(theta)
    y = y + speed * math.sin(theta)
    if (x - 5 < to_x < x + 5) and (y - 5 < to_y < y + 5):
        is_moving = 0


hide_cursor()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(hand_x + 25 , hand_y - 26)
    character.clip_draw(frame * 100, direction * 100, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    if(is_moving == 1):
        move_to()
    handle_events()
    delay(0.05)



close_canvas()