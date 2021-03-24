import pygame, random


class Ball:
    ''' class for the ball '''
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.ball_color
        self.radius = self.settings.ball_radius

        self.reset_ball() # Places the ball to the center of the screen
        self.draw_ball() # Draws the ball 

        self.direction_x = self.ball_direction() # random x direction
        self.direction_y = self.ball_direction() # random y direction
    
    def draw_ball(self):
        ''' Draws the ball to the screen'''
        pygame.draw.circle(self.screen, self.color,
            (self.ball_pos_x, self.ball_pos_y), self.radius)
    
    def update(self):
        ''' Moves the ball every frame '''
        self.x += self.settings.ball_speed_x * self.direction_x
        self.y += self.settings.ball_speed_y * self.direction_y

        self.ball_pos_x = self.x
        self.ball_pos_y = self.y

    def ball_direction(self):
        paddle_mid = (self.settings.screen_height // 2) - (self.settings.paddle_height // 2)
        if self.ball_pos_y <= paddle_mid:
            return -1
        elif self.ball_pos_y >= paddle_mid:
            return 1

        # if self.ball_pos_y >= self.settings.screen_height // 2:
        #     return -1
        # elif self.ball_pos_y <= self.settings.screen_height // 2:
        #     return 1

    def random_ball_direction(self):
        ''' Random ball direction '''
        return random.choice([1, -1])

    def check_borders(self):
        ''' check if ball collides with the top and bottom borders '''
        if self.y >= self.settings.screen_height or self.y <= 0:
            return True

    def reset_ball(self):
        ''' Places the ball in the center of the screen '''
        self.ball_pos_x = self.settings.ball_pos_x
        self.ball_pos_y = self.settings.ball_pos_y
        self.x = float(self.ball_pos_x)
        self.y = float(self.ball_pos_y)
