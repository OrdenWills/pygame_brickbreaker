import pygame

class Button:
    def __init__(self,color,txt,size) -> None:
        self.font = pygame.font.Font(None,size)
        self.txt = self.font.render(txt,True,color)
        self.rect = self.txt.get_rect()
        