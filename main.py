import pygame
from settings import Settings
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from game_stats import GameStats
from score import Score_board
from screens import Screen
from buttons import Button
import time


pygame.init()


clock = pygame.time.Clock()


class Breaker:
    def __init__(self) -> None:
        self.settings = Settings()
        self.window = pygame.display.set_mode(
            (self.settings.width, self.settings.height), pygame.SRCALPHA)
        self.wind_rect = self.window.get_rect()
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = pygame.sprite.Group()
        self.stats = GameStats()
        self.score = Score_board(self)
        self.screen = Screen()
        self.game_active = self.stats.game_active
        self._show_bricks()

    def run_game(self):
        """The game loop"""
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                self._check_event_type(event)

            self.update_screen()

    def _check_event_KD(self, event):
        """listens for event keydown"""
        # if self.game_active:
        if event.key == pygame.K_LEFT:
            self.paddle.left = True
        if event.key == pygame.K_RIGHT:
            self.paddle.right = True
        self.paddle.move()
        # To exit the game with keyboard
        if event.key == pygame.K_ESCAPE:
            exit()
        # Space key listens to start game
        if not self.game_active and self.screen.screen2:
            if event.key == pygame.K_SPACE:
                self.game_active = True

    def _check_mouse_event(self,event):
        if event.pos[0] >= 450 and event.pos[0] <= 574 and event.pos[1] >= 272 and event.pos[1] <= 320:
            self.screen.screen1 = False
            self.screen.screen2 = True
        elif event.pos[0] >= 453 and event.pos[0] <= 571 and event.pos[1] >= 360 and event.pos[1] <= 408:
            exit()


    def _check_event_KU(self, event):
        """listens for event keyup """
        if event.key == pygame.K_LEFT:
            self.paddle.left = False
        if event.key == pygame.K_RIGHT:
            self.paddle.right = False

    def _check_event_type(self, event):
        """listens for event types"""
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            self._check_event_KD(event)
        elif event.type == pygame.KEYUP:
            self._check_event_KU(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._check_mouse_event(event)
    def ball_paddle_collision(self):
        """checks if theres collision between the paddle and the ball"""
        if (self.paddle.rect.colliderect(self.ball.rect)):
            self.settings.ball_dy *= -1

    def ball_brick_collision(self):
        """checks if there's collision between the ball and the brick(s)"""
        for b in self.bricks:
            if self.ball.rect.colliderect(b.rect):
                self.bricks.remove(b)
                self.settings.ball_dy *= -1
                self.score.update_score()

    def _create_brick(self,num_row,num_col):
        brick = Bricks(self)
        width, heigth = brick.rect.size
        brick.x = width + (2 + width) * num_row
        brick.rect.x = brick.x
        brick.rect.y = self.ball.radius + heigth + (2 + heigth) * num_col
        self.bricks.add(brick)

    def _show_bricks(self):
        brick = Bricks(self)
        width, height = brick.rect.size
        available_width = (self.wind_rect.width) - width + 2
        brick_num = available_width // (2 + width)
        available_height = round((self.wind_rect.height // height)/4)
        # print(available_width,available_height)

        for num_col in range(available_height):
            for num_row in range(brick_num):
                self._create_brick(num_row,num_col)

    def play_button(self):
        button = Button(self.settings.text_color,f"PLAY",70)
        button.rect.centerx = self.wind_rect.centerx
        button.rect.centery = self.wind_rect.height // 3 + 40
        
        # print(button.rect.top , button.rect.bottom)
        return button.txt, button.rect
    
    def intro_text(self):
        text = Button((244,100,0),"Brick Breaker",100)
        text.rect.centerx = self.wind_rect.centerx
        text.rect.centery = self.wind_rect.height // 5
        return text.txt, text.rect
        
    def Quit_button(self):
        button = Button(self.settings.text_color,f"QUIT",70)
        button.rect.centerx = self.wind_rect.centerx
        button.rect.centery = self.wind_rect.centery
        return button.txt, button.rect

    def active_screen(self):
        img = pygame.image.load('./images/bg.jpg')
        bg_img = pygame.transform.scale(img,self.wind_rect.size)
        return bg_img

    def update_screen(self):
        """updates the screen also responsible for drawing new rects to the screen"""
        # pygame.draw.circle(self.window,red,(x,y),radius)
        self.window.fill((0, 0, 0))
        self.ball.blit_me()
        self.paddle.blit_me()
        self.score.blit_me()
        self.bricks.draw(self.window)
        if self.screen.screen1:
            self.window.blit(self.active_screen(),(0,0))
            self.window.blit(self.intro_text()[0],self.intro_text()[1])
            self.window.blit(self.play_button()[0],self.play_button()[1])
            self.window.blit(self.Quit_button()[0],self.Quit_button()[1])
        elif self.screen.screen2:
            if self.game_active:
                self.ball_paddle_collision()
                self.ball_brick_collision()
                self.ball.bounce_ball()
            else:
                self.ball.reset_ball()
        else:
            self.ball.reset_ball()
            
            self.ball
        pygame.display.update()


game = Breaker()
game.run_game()
