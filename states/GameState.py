import pygame as pg

class GameState:
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = ""

        font_path = "assets/fonts/Roboto-Regular.ttf"
        self.font_small = pg.font.Font(font_path, 30)
        self.font_large = pg.font.Font(font_path, 100)

    def handle_events(self, events): ...

    def update(self, dt): ...

    def render(self, screen): ...
