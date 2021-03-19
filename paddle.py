import pygame

class Paddle:
    ''' Class for paddle '''
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.color = game.settings.paddle_color
        
        # Make a rectangle for the paddle
        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)

        # Flags so the paddles dont move instant
        self.moving_up = False
        self.moving_down = False

        self.y = float(self.rect.y)

    def draw_paddle(self):
        ''' draw paddle to screen '''
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        ''' for keymovements move paddle'''
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom <= self.settings.screen_height:
            self.y += self.settings.paddle_speed

        self.rect.y = self.y

class PaddleLeft(Paddle):
    ''' Class for left paddle '''
    def __init__(self, game):
        super().__init__(game)
        self.reset_paddle()
    
    def reset_paddle(self):
        ''' Place paddle to the right spot and if goal scored reset paddle '''

        # Place the paddle to the middle left of the screen
        self.rect.midleft = self.screen_rect.midleft 
        self.rect.x += 50
        self.y = float(self.rect.y)

class PaddleRight(Paddle):
    ''' Class for the right paddle '''
    def __init__(self, game):
        super().__init__(game)
        self.reset_paddle()

    def reset_paddle(self):
        ''' Place paddle to the left spot and if goal scored reset paddle'''

        # Place the paddle to the middle right of the screen
        self.rect.midright = self.screen_rect.midright
        self.rect.x -= 50
        self.y = float(self.rect.y)
