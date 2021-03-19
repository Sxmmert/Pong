from random import choice


class Settings:
    def __init__(self):
        ''' Initialize settings '''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_color = (255, 255, 255)
        self.paddle_width = 20
        self.paddle_height = self.screen_height // 4

        # Middle line settings
        self.middle_line_color = (255, 255, 255)
        self.middle_line_width = 5

        # Ball settings
        self.ball_color = (255, 255, 255)
        self.ball_radius = 15
        self.ball_pos_x = self.screen_width // 2 
        self.ball_pos_y = self.screen_height // 2

        # Move the ball to left or right
        # 1 is right, -1 is left
        self.directions = [1, -1]

        # Player scores
        self.player_left_score = 0
        self.player_right_score = 0

        # Default speed settings ball and paddle
        self.reset_settings()

    def reset_settings(self):
        ''' Default speed settings '''
        self.paddle_speed = 0.75
        self.ball_speed_x = 0.50
        self.ball_speed_y = 0.25

    def speedup_ball(self):
        ''' every collission with paddle '''
        if not self.ball_speed_x >= 1.9:
            self.ball_speed_x *= 1.1
            self.ball_speed_y *= 1.1
