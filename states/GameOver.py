import pygame as pg
from states.GameState import GameState

class GameOver(GameState):
    def __init__(self):
        super().__init__()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.done = True
                    self.next_state = "MENU"

    def render(self, screen):
        screen.fill(pg.Color("orange"))

        width, height = screen.get_width(), screen.get_height()

        text_state = self.font_large.render("Game over", True, pg.Color("orangered3"))
        text_state_rect = text_state.get_rect(center=(width/2, height/2))
        screen.blit(text_state, text_state_rect)

        text_info = self.font_small.render("Press SPACE to change the game state", True, pg.Color("orangered3"))
        text_info_rect = text_info.get_rect(center=(width/2, height/2+100))
        screen.blit(text_info, text_info_rect)