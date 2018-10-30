
import game_framework
from pico2d import *

import game_world


class Fluid_exit:

    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


class Ghost:
    image = None
    def __init__(self, boy):
        self.x, self.y = boy.x, boy.y
        self.image = load_image('animation_sheet.png')
        self.dir = boy.dir
        self.frame = boy.frame
        self.event_que = []
        self.cur_state = Fluid_exit()
    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        pass

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass





