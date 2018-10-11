import game_framework
from pico2d import *
import main_state

name = "paued"
image = None
blinking = 0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    delay(0.01)
    pass


def draw():
    global blinking
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if (blinking < 20):
       image.draw(400, 300)
    blinking = (blinking + 1) % 30
    update_canvas()



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def pause():
    pass


def resume():
    pass