
import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3)
EXIT_SPEED_MPS = 0.1
EXIT_SPEED_PPS = EXIT_SPEED_MPS * PIXEL_PER_METER
FADE_SPEED_PPS = 0.4 / 3 * PIXEL_PER_METER
WAKE_UP_PPS = 2 / 3 * PIXEL_PER_METER

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
        ghost.transparent -= FADE_SPEED_PPS * game_framework.frame_time
        ghost.degree -= WAKE_UP_PPS * game_framework.frame_time
        if ghost.y - ghost.origin_y >= 3 * PIXEL_PER_METER:
            ghost.y = ghost.origin_y + 3 * PIXEL_PER_METER
            ghost.add_event(GO_CIRCLE)


    @staticmethod
    def draw(ghost):
        if ghost.dir == 1:
            ghost.image.clip_composite_draw(int(ghost.frame) * 100, 300, 100, 100, 3.141592 / ghost.degree, '', ghost.x - 25, ghost.y - 25, 100, 100)
        else:
            ghost.image.clip_composite_draw(int(ghost.frame) * 100, 200, 100, 100, -3.141592 / ghost.degree, '', ghost.x + 25, ghost.y - 25, 100, 100)

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
next_state_table = {
    Fluid_exit:{GO_CIRCLE: Circles_around},
    Circles_around:{}
}

class Ghost:
    image = None
    def __init__(self, boy):
        self.x, self.y = boy.x, boy.y
        self.origin_y = boy.y
        self.image = load_image('animation_sheet.png')
        self.dir = boy.dir
        self.frame = boy.frame
        self.event_que = []
        self.cur_state = Fluid_exit

        self.degree = 2
        self.transparent = 0.9
        self.cur_state.enter(self)
    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass





