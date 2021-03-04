import pygame, sys
from settings import Settings
from paddle import PaddleLeft, PaddleRight
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard
from button import Button


class Pong:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # FULLSCREEN
        pygame.display.set_caption('Pong')
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.scoreboard = ScoreBoard(self)
        self.button = Button(self, 'Play')

        self.paddle_left = PaddleLeft(self)
        self.paddle_right = PaddleRight(self)
        self.ball = Ball(self)

        self.playing = False

    def main(self):
        while True:
            self._check_events()
            if self.playing:
                self._update_paddle()
                self._ball_update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_event_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_event_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_event_keydown(self, event):
        if event.key == pygame.K_w:
            self.paddle_left.moving_up = True
        elif event.key == pygame.K_s:
            self.paddle_left.moving_down = True

        elif event.key == pygame.K_UP:
            self.paddle_right.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.paddle_right.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self.playing = True

    def _check_event_keyup(self, event):
        if event.key == pygame.K_w:
            self.paddle_left.moving_up = False
        elif event.key == pygame.K_s:
            self.paddle_left.moving_down = False

        elif event.key == pygame.K_UP:
            self.paddle_right.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.paddle_right.moving_down = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.playing:
            self.playing = True

    def _update_paddle(self):
        self.paddle_right.update()
        self.paddle_left.update()

    def _ball_update(self):
        # Check collission borders
        if self.ball.check_borders():
            self.ball.direction_y *= -1
        
        # Check collission paddles and ball
        self._collission_ball_paddle()

        # Check collissions goals
        self._collission_end_border()

        self.ball.update()

    def _reset(self):
        self.paddle_left.reset_paddle()
        self.paddle_right.reset_paddle()
        self.settings.reset_settings()
        self.ball.reset_ball()
        self.ball.direction_x *= 1
        sleep(1)

    def _collission_ball_paddle(self):
        ball_left_paddle_collission = (self.ball.ball_pos_x <= self.paddle_left.rect.right) and (self.ball.ball_pos_x >= self.paddle_left.rect.left) and (self.ball.ball_pos_y <= self.paddle_left.rect.bottom) and (self.ball.ball_pos_y >= self.paddle_left.rect.top)
        ball_right_paddle_collission = (self.ball.ball_pos_x <= self.paddle_right.rect.right) and (self.ball.ball_pos_x >= self.paddle_right.rect.left) and (self.ball.ball_pos_y <= self.paddle_right.rect.bottom) and (self.ball.ball_pos_y >= self.paddle_right.rect.top)\

        if ball_right_paddle_collission or ball_left_paddle_collission:
            self.ball.direction_x *= -1
            self.ball.direction_y = self.ball.ball_direction()
            self.settings.speedup_ball()

    def _collission_end_border(self):
        left_border = self.ball.ball_pos_x <= 0
        right_border = self.ball.ball_pos_x >= self.settings.screen_width
        if left_border:
            self.settings.player_right_score += 1
            self.scoreboard.prep_score_player_right()
            self._reset()
        elif right_border:
            self.settings.player_left_score += 1
            self.scoreboard.prep_score_player_left()
            self._reset()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_middle_line()
        self.ball.draw_ball()
        self.paddle_left.draw_paddle()
        self.paddle_right.draw_paddle()
        if not self.playing:
            self.button.draw_button()
        self.scoreboard.show_score()
        pygame.display.flip()

    def _draw_middle_line(self):
        COLOR = self.settings.middle_line_color
        WIDTH = self.settings.middle_line_width
        START_POS = (self.settings.screen_width // 2, 0)
        END_POS = (self.settings.screen_width // 2, self.settings.screen_height)
        pygame.draw.line(self.screen, COLOR, START_POS, END_POS, WIDTH)

if __name__ == '__main__':
    pong = Pong()
    pong.main()
