import pygame
from pygame.sprite import Sprite


class Bricks(Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        self.screen = game.window
        img = pygame.image.load("./images/brick.jpg")
        self.image = pygame.transform.scale(img,(img.get_width()//3,img.get_height()//3))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        # print(self.rect.size)
        # print(self.image.get_width())
        