import pygame

class Score_board:
    def __init__(self,game) -> None:
        self.game = game
        self.screen = game.window
        self.settings = game.settings
        self.score = 0
        self.font = pygame.font.Font(None,30)
        self.update_score()
        self.rect = self.text.get_rect()
        self.rect.top = self.game.wind_rect.top
        self.rect.centerx = self.game.wind_rect.centerx
        
        
    
    def update_score(self):
        self.text = self.font.render(f"Score: {self.score}",True,self.settings.text_color)
        self.score += 1

    def blit_me(self):
        self.screen.blit(self.text,self.rect)

