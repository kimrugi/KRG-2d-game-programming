
import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3)
EXIT_SPEED_PPS = 1 * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

GO_CIRCLE = range(1)

class Fluid_exit:

    @staticmethod
    def enter(ghost):
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do(ghost):
        ghost.y += EXIT_SPEED_PPS * game_framework.frame_time
        if ghost.y >= 3 * PIXEL_PER_METER:
            ghost.add_event(GO_CIRCLE)


    @staticmethod
    def draw():
        pass

class Circles_around:

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
        self.cur_state = Fluid_exit

        self.transparent = 0.9
        self.cur_state.enter(self)
    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        pass

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass





