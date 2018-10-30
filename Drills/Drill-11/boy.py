from pico2d import *
from ball import Ball

import game_world

# Boy Event
<<<<<<< HEAD
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)
=======
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, TIRED, SHIFT_DOWN, SHIFT_UP, GO_DASH = range(10)
DASH_SPEED = 2
MAX_STAMINA = 100
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
<<<<<<< HEAD
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
=======
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): SHIFT_UP
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
}


# Boy States
<<<<<<< HEAD
class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        # fill here
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        # fill here

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                         3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
=======
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
<<<<<<< HEAD
        boy.timer = 100
=======
        boy.timer = 300
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
<<<<<<< HEAD
=======
        elif event == SHIFT_UP:
            pass
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
        pass

    @staticmethod
    def do(boy):
<<<<<<< HEAD
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
=======
        boy.frame = (boy.frame + 1) % 40
        boy.timer -= 1
        if boy.stamina < MAX_STAMINA:
            boy.stamina += 1
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
<<<<<<< HEAD
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)
=======
            boy.image.clip_draw(boy.frame // 5 * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame // 5 * 100, 200, 100, 100, boy.x, boy.y)
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
<<<<<<< HEAD
=======
        elif event == SHIFT_UP:
            pass
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 40
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)
<<<<<<< HEAD
=======
        if boy.stamina < MAX_STAMINA:
            boy.stamina += 1
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame // 5 * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame // 5 * 100, 0, 100, 100, boy.x, boy.y)


<<<<<<< HEAD
class DashState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity
        boy.timer = 200
        pass

    @staticmethod
    def exit(boy, event):
=======
class SleepState:
    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        if event == SHIFT_UP:
            pass
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
        pass

    @staticmethod
    def do(boy):
<<<<<<< HEAD
        pass

    @staticmethod
    def draw(boy):
        pass


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState}
}


=======
        boy.frame = (boy.frame + 1) % 40
        if boy.stamina < MAX_STAMINA:
            boy.stamina += 1

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame // 5 * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25,
                                                boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame // 5 * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

    pass

class DashState:
    @staticmethod
    def enter(boy, event):
        pass

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
            pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % (40 // DASH_SPEED)
        boy.stamina -= 1
        boy.x += boy.velocity * DASH_SPEED
        boy.x = clamp(25, boy.x, 1600 - 25)
        if boy.stamina == 0:
            boy.add_event(TIRED)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw((boy.frame * 2 // 5) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw((boy.frame * 2 // 5) * 100, 0, 100, 100, boy.x, boy.y)

    pass




next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, SPACE: IdleState, SHIFT_DOWN: IdleState, SHIFT_UP: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE: RunState, SHIFT_DOWN: DashState, SHIFT_UP: RunState, GO_DASH: DashState},
    SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                 SPACE: SleepState, SHIFT_UP: SleepState, SHIFT_DOWN: SleepState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SPACE: DashState, SHIFT_DOWN: DashState, SHIFT_UP: RunState, TIRED: RunState}
}

>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
<<<<<<< HEAD
=======
        self.stamina = MAX_STAMINA
>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

<<<<<<< HEAD
    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)
=======

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)
        pass


>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305

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

<<<<<<< HEAD
=======

>>>>>>> d2272f6385271e1cbc5075b41547bce36ef77305
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
