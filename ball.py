import pygame, random


class Ball:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.ball_color
        self.radius = self.settings.ball_radius
        self.reset_ball()
        self.draw_ball()

        self.direction_x = self.ball_direction()
        self.direction_y = self.ball_direction()
    
    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color,
            (self.ball_pos_x, self.ball_pos_y), self.radius)

    def random_y(self):
        return random.random() / 7
    
    def update(self):
        self.x += self.settings.ball_speed_x * self.direction_x
        self.y += self.settings.ball_speed_y * self.direction_y

        self.ball_pos_x = self.x
        self.ball_pos_y = self.y

    def ball_direction(self):
        return random.choice([1, -1])

    def check_borders(self):
        if self.y >= self.settings.screen_height or self.y <= 0:
            return True

    def reset_ball(self):
        self.ball_pos_x = self.settings.ball_pos_x
        self.ball_pos_y = self.settings.ball_pos_y
        self.x = float(self.ball_pos_x)
        self.y = float(self.ball_pos_y)
