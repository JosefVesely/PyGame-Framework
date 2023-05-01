import pygame as pg

class Input:
    def __init__(self, default_value, pos: pg.Vector2, width, height, 
                 center: pg.Vector2=None, font_size=16,
                 text_color=pg.Color("black"), bg_color=pg.Color("darkgray")):
        
        if center: 
            self.rect = pg.Rect(0, 0, width, height)
            self.rect.center = center
        else:
            self.rect = pg.Rect(pos.x, pos.y, width, height)

        self.text_color = text_color
        self.bg_color = bg_color
        self.font_size = font_size

        self.value = default_value
        self.clicked = False
        self.hovered = False

    def handle_events(self, events): ...

    def update(self):...

    def render(self, screen):
        if self.clicked:
            pg.draw.rect(screen, pg.Color("green2"), self.rect)
        elif self.hovered:
            pg.draw.rect(screen, pg.Color("white"), self.rect)
        else:
            pg.draw.rect(screen, self.bg_color, self.rect)

        # Text
        self.font = pg.font.Font(None, 30)

        text = self.font.render(self.value, True, self.text_color)

        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)