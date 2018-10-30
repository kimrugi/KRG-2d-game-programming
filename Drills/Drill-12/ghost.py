
import game_framework
from pico2d import *

import game_world





class Ghost:
    image = None
    def __init__(self, boy):
        self.x, self.y = boy.x, boy.y
        self.image = load_image('animation_sheet.png')
        self.dir = boy.dir
        self.frame = boy.frame
        self.event_que = []




