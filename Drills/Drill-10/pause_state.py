import game_framework
from pico2d import *
import title_state

name = "paued"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    pass


def draw():
    pass




def handle_events():
    pass


def pause():
    pass


def resume():
    pass