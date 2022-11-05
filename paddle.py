import pygame

class Paddle:
    def __init__(self,game) -> None:
        self.screen = game.window
        self.settings = game.settings
        self.Screen_rect = game.wind_rect
        paddle =  pygame.image.load('./images/paddle.png')
        self.paddle = pygame.transform.scale(paddle,(paddle.get_width()//2,paddle.get_height()//2))
        self.rect = self.paddle.get_rect()
        self.reset_paddle()
        self.left = False
        self.right = False
        self.dx = 20
        
    def blit_me(self):
        self.screen.blit(self.paddle,self.rect)

    def move(self):
        if (self.right) and (self.rect.right <= self.settings.width - self.settings.radius):
            self.x += self.dx
        if (self.left) and (self.rect.left >= self.settings.radius):
            self.x -= self.dx
        self.rect.x = self.x

    def reset_paddle(self):
        self.rect.centerx = self.Screen_rect.centerx
        self.rect.bottom = self.Screen_rect.bottom
        self.x = self.rect.x