import pygame as pg
import time
import sys

from states.Menu import Menu
from states.MainGame import MainGame
from states.GameOver import GameOver
from states.GUIWidgets import GUIWidgets

class Game:
    def __init__(self):
        # Constants
        TITLE = "PyGame Framework"
        WINDOW_WIDTH = 700
        WINDOW_HEIGHT = 500
        self.MAX_FPS = 60

        # Initialize PyGame
        pg.init()
        pg.display.set_caption(TITLE)
        pg.display.set_icon(pg.image.load("assets/images/icon.png"))

        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pg.time.Clock()
        self.done = False
        
        # Delta time
        self.dt = 0
        self.now = 0
        self.prev_time = 0

        # Game state
        self.states = {
            "MENU": Menu(),
            "WIDGETS": GUIWidgets(),
            "MAINGAME": MainGame(),
            "GAMEOVER": GameOver(),
        }
        self.state = self.states["MENU"]

    def run(self): 
        while not self.done:
            self.clock.tick(self.MAX_FPS)
            self.handle_events()
            self.update()
            self.render()
            pg.display.update()

    def handle_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        self.state.handle_events(events)
    
    def update_dt(self):
        self.now = time.time()
        self.dt = self.now - self.prev_time
        self.prev_time = self.now

    def update(self):
        self.update_dt()

        if self.state.quit:
            self.done = True
        elif self.state.done:
            next_state = self.state.next_state

            if next_state == "":
                raise ValueError("Next game state is not defined")

            self.state.done = False
            self.state = self.states[next_state]
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)


        self.state.update(self.dt)

    def render(self):
        self.state.render(self.screen)
