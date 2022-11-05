import pygame

class Ball:
    def __init__(self,game) -> None:
        self.game = game
        self.screen = game.window
        self.screen_rect = game.wind_rect
        self.settings = game.settings
        self.paddle = game.paddle
        img = pygame.image.load("./images/ball.png")
        self.image = pygame.transform.scale(img,(img.get_width()//4,img.get_height()//4))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2
        self.reset_ball()


    def blit_me(self):
        self.screen.blit(self.image,self.rect)
    
    def bounce_ball(self):
        self.x += self.settings.ball_dx
        self.y += self.settings.ball_dy
        if (self.x < self.radius) or (self.x > self.settings.width - self.radius):
            self.settings.ball_dx *= -1
        if (self.y < self.radius):
            self.settings.ball_dy *= -1
        if (self.y > self.settings.height - self.radius):
        # if (self.y > self.paddle.rect.centery):
            self.paddle.reset_paddle()
            self.reset_ball()
        self.rect.centerx = self.x
        self.rect.centery = self.y
    def reset_ball(self):
        self.rect.bottom = self.paddle.rect.top
        self.rect.centerx = self.paddle.rect.centerx
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.game.game_active = False