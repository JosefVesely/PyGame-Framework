import pygame as pg
from states.GameState import GameState
from utils.Button import Button
from utils.Input import Input

class GUIWidgets(GameState):
    def __init__(self):
        super().__init__()
        
        self.button = Button("Click me!", None, 250, 50, center=pg.Vector2(350, 50), font_size=30)
        self.input = Input("Enter text", None, 250, 50, center=pg.Vector2(350, 150), font_size=30)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.done = True
                    self.next_state = "MENU"

        self.button.handle_events(events)
        self.input.handle_events(events)

    def update(self, dt):
        self.button.update()
        self.input.update()

    def render(self, screen):
        screen.fill(pg.Color("pink"))

        width, height = screen.get_width(), screen.get_height()

        text_info = self.font_small.render("Press SPACE to go back", True, pg.Color("orangered4"))
        text_info_rect = text_info.get_rect(center=(width/2, height/2+100))
        screen.blit(text_info, text_info_rect)

        self.button.render(screen)
        self.input.render(screen)
