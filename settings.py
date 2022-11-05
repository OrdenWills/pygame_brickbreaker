
import pygame

WIDTH = 600
HEIGHT = 600

colors = [(100,200,255),(255,100,150),(200,200,200)]

class Settings:
    def __init__(self) -> None:
        # Screen Settings 
        self.width = WIDTH
        self.height = HEIGHT
        # Ball x,y co-ordinate and dx,dy
        self.ball_x = 100
        self.ball_y = 100
        self.ball_dx = 5
        self.ball_dy = 7
        # Ball radius
        self.radius = 8
        # Game status
        self.game_active = False


        blue = pygame.Color(*colors[0])
        red = pygame.Color(*colors[1])
