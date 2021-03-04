import pygame


class PaddleLeft:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.color = game.settings.paddle_color

        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        
        self.reset_paddle()

        self.moving_up = False
        self.moving_down = False

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom <= self.settings.screen_height:
            self.y += self.settings.paddle_speed

        self.rect.y = self.y

    def reset_paddle(self):
        self.rect.midleft = self.screen_rect.midleft
        self.rect.x += 50
        self.y = float(self.rect.y)

class PaddleRight(PaddleLeft):
    def __init__(self, game):
        super().__init__(game)
        self.reset_paddle()

    def reset_paddle(self):
        self.rect.midright = self.screen_rect.midright
        self.rect.x -= 50
        self.y = float(self.rect.y)
