import random
from pico2d import *
import game_world
import game_framework
import main_state
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(400, 1600-1), random.randint(300, 1200-1)
        self.bg = main_state.get_background()

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)

    def update(self):
        pass

