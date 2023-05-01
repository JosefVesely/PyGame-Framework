import pygame as pg
from states.GameState import GameState
from utils.Button import Button

class Menu(GameState):
    def __init__(self):
        super().__init__()

        self.button = Button("Preview GUI widgets", None, 300, 50, center=pg.Vector2(350, 100), 
                             font_size=40, text_color=pg.Color("darkblue"), bg_color=pg.Color("dodgerblue"))

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.done = True
                    self.next_state = "MAINGAME"

        self.button.handle_events(events)

        if self.button.clicked:
            self.done = True
            self.next_state = "WIDGETS"

    def update(self, dt):
        self.button.update()

    def render(self, screen):
        screen.fill(pg.Color("lightblue"))

        width, height = screen.get_width(), screen.get_height()

        text_state = self.font_large.render("Menu", True, pg.Color("dodgerblue3"))
        text_state_rect = text_state.get_rect(center=(width/2, height/2))
        screen.blit(text_state, text_state_rect)

        text_info = self.font_small.render("Press SPACE to change the game state", True, pg.Color("dodgerblue3"))
        text_info_rect = text_info.get_rect(center=(width/2, height/2+100))
        screen.blit(text_info, text_info_rect)

        self.button.render(screen)
