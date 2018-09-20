from pico2d import *
import math

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDHT, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow')
speed = 5
running = 1

hand_x, hand_y = KPU_WIDTH // 2, KPU_HEIGHT // 2

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            hand_x, hand_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


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
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        animation_character(theta)
        frame = (frame + 1) % 8
        update_canvas()
        x = x + speed * math.cos(theta)
        y = y + speed * math.sin(theta)
        delay(0.05)


while running:
    frame = 0


close_canvas()