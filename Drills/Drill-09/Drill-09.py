from pico2d import *
import random
running = 0
WIDTH = 800
HEIGHT = 600

# y = 599


class Ball:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = 599
        self.speed = random.randint(1, 100) / 10
        self.falling = 1
        if random.randint(0, 1):
            self.image = load_image('ball21x21.png')
            self.size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.size = 41

    def check(self):
        if (self.y - self.size // 2) < 60:
            self.falling = 0

    def fall(self):
        if self.falling:
            self.y = self.y - self.speed
            self.check()

    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(0, 300)
        self.frame = 0

    def move(self):
        self.x = self.x + 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, 90)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(WIDTH, HEIGHT);
boy = [Boy() for i in range(11)]
grass = Grass()
balls = [Ball() for i in range(20)]


running = 1
while running:
    handle_events()
    clear_canvas()
    for i in boy:
        i.draw()
    for i in balls:
        i.draw()
    grass.draw()
    update_canvas()

    for i in boy:
        i.move()
        i.frame = (i.frame + 1) % 8
    for i in balls:
        i.fall()

close_canvas()