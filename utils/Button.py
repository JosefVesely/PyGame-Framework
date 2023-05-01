import pygame as pg

class Button:
    def __init__(self, text, pos: pg.Vector2, width, height, 
                 center: pg.Vector2=None, font_size=16,
                 text_color=pg.Color("black"), bg_color=pg.Color("darkgray")):
        
        if center: 
            self.rect = pg.Rect(0, 0, width, height)
            self.rect.center = center
        else:
            self.rect = pg.Rect(pos.x, pos.y, width, height)

        self.text = text
        self.text_color = text_color
        self.bg_color = bg_color
        self.font_size = font_size

        self.clicked = False
        self.hovered = False

    def render(self, screen):
        # Button
        if self.clicked:
            pg.draw.rect(screen, pg.Color("green2"), self.rect)
        elif self.hovered:
            pg.draw.rect(screen, pg.Color("white"), self.rect)
        else:
            pg.draw.rect(screen, self.bg_color, self.rect)

        # Text
        self.font = pg.font.Font(None, self.font_size)

        text = self.font.render(self.text, True, self.text_color)

        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def update(self):
        if self.hovered:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

    def handle_events(self, events):
        self.clicked = False
        self.hovered = False

        mouse_pos = pg.mouse.get_pos()

        if pg.Rect.collidepoint(self.rect, mouse_pos):
            self.hovered = True

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.Rect.collidepoint(self.rect, mouse_pos):
                    self.clicked = True

    def set_center(self, x, y):
        self.rect.center = (x, y)