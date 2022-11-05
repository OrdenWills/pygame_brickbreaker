import pygame
from settings import Settings
from paddle import Paddle
from ball import Ball
from bricks import Bricks
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
        self.game_active = self.settings.game_active
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
        if not self.game_active:
            if event.key == pygame.K_SPACE:
                self.game_active = True

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

    def _create_brick(self,num_row,num_col):
        brick = Bricks(self)
        width, heigth = brick.rect.size
        brick.rect.x = num_row
        brick.rect.y = num_col
        self.bricks.add(brick)

    def _show_bricks(self):
        brick = Bricks(self)
        width, height = brick.rect.size
        available_width = self.wind_rect.width // width
        available_height = round((self.wind_rect.height // height)/2)
        print(available_width,available_height)

        for row in range(available_width):
            for col in range(8):
                num_row = width * row
                num_col = height * col
                self._create_brick(num_row,num_col)


        

    def update_screen(self):
        """updates the screen also responsible for drawing new rects to the screen"""
        # pygame.draw.circle(self.window,red,(x,y),radius)
        self.window.fill((0, 0, 0))
        self.ball.blit_me()
        self.paddle.blit_me()
        # self._show_bricks()
        self.bricks.draw(self.window)
        if self.game_active:
            self.ball_paddle_collision()
            self.ball_brick_collision()
            self.ball.bounce_ball()
        else:
            self.ball.reset_ball()
            # self.ball
        pygame.display.update()


game = Breaker()
game.run_game()
