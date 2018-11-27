import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

from boy import Boy
from zombie import Zombie
import world_build_state
PIXEL_PER_METER = 100 / 3

middle_x, middle_y = int(40 * PIXEL_PER_METER) // 2, int(30 * PIXEL_PER_METER) // 2

show_y = ((middle_y * 2) - 100) / 11


ranking_list = []
name = "WorldBuildState"
font = None
menu = None

def enter():
    global font
    font = load_font('ENCR10B.TTF', 20)
    score = main_state.get_score()
    ranking_list.append(score)
    ranking_list.sort()

    pass

def exit():
    global font
    del font
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(world_build_state)
def update():
    pass

def draw():
    clear_canvas()
    font.draw(middle_x, show_y * 11, '[Total Ranking]', (0,0,0))
    i = 10
    for score in ranking_list:
        font.draw(middle_x, show_y * i, '#%d. %3.2f' % (i, score), (0,0,0))
    update_canvas()


