from pico2d import *
running = 0

# y = 599
class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = 0
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, 30)


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


open_canvas(1280, 720);
boy = Boy()
grass = Grass()

running = 0
while running:
    handle_events()
    boy.draw()
    grass.draw()
    boy.frame = (boy.frame + 1) % 4

close_canvas()