from random import choice


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.paddle_color = (255, 255, 255)
        self.paddle_width = 20
        self.paddle_height = 300

        self.middle_line_color = (255, 255, 255)
        self.middle_line_width = 5

        self.ball_color = (255, 255, 255)
        self.ball_radius = 15
        self.ball_pos_x = self.screen_width // 2 
        self.ball_pos_y = self.screen_height // 2

        self.directions = [1, -1]

        self.player_left_score = 0
        self.player_right_score = 0

        self.reset_settings()

    def reset_settings(self):
        self.paddle_speed = 1.5
        self.ball_speed_x = 0.15
        self.ball_speed_y = 0.08

    def speedup_ball(self):
        self.ball_speed_x *= 1.1
        self.ball_speed_y += 0.01
