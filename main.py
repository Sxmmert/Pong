import pygame
import sys

from settings import Settings
from paddle import PaddleLeft, PaddleRight
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard
from button import Button


class Pong:
    ''' Main class for the game '''
    def __init__(self):
        pygame.init() # Initialize all of pygame
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # FULLSCREEN

        pygame.display.set_caption('Pong') # Title 
        self.settings.screen_width = self.screen.get_rect().width # Screen width
        self.settings.screen_height = self.screen.get_rect().height # Screen height

        self.scoreboard = ScoreBoard(self)
        self.button = Button(self, 'Play') # make a button with {text} on it

        self.paddle_left = PaddleLeft(self)
        self.paddle_right = PaddleRight(self)
        self.ball = Ball(self)

        self.playing = False # Flag, when False show play button, else play the game

    def main(self):
        ''' Main game loop '''
        while True:
            self._check_events()
            if self.playing:
                self._update_paddle()
                self._ball_update()
            self._update_screen()

    def _check_events(self):
        ''' Check for keyboard and mouse events '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit the game
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Button pressed down
                self._check_event_keydown(event)
            elif event.type == pygame.KEYUP: # Button released
                self._check_event_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: # Mouse button clicked
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_event_keydown(self, event):
        ''' Keyboard key pressed down '''
        # Left Paddle Movements
        if event.key == pygame.K_w:
            self.paddle_left.moving_up = True
        elif event.key == pygame.K_s:
            self.paddle_left.moving_down = True

        # Right Paddle Movements
        elif event.key == pygame.K_UP:
            pass
            self.paddle_right.moving_up = True
        elif event.key == pygame.K_DOWN:
            pass
            self.paddle_right.moving_down = True

        # Alternative to quit the game
        elif event.key == pygame.K_q:
            sys.exit()

        # Alternative to the mouse click
        elif event.key == pygame.K_p:
            self.playing = True
            pygame.mouse.set_visible(False)

    def _check_event_keyup(self, event):
        ''' Keyboard key released '''
        if event.key == pygame.K_w:
            self.paddle_left.moving_up = False
        elif event.key == pygame.K_s:
            self.paddle_left.moving_down = False

        elif event.key == pygame.K_UP:
            self.paddle_right.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.paddle_right.moving_down = False

    def _check_play_button(self, mouse_pos):
        ''' Check if mouse click collided with the play button '''
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.playing:
            self.playing = True
            pygame.mouse.set_visible(False) # Set cursor to invisible

    def _update_paddle(self):
        ''' Move the paddles '''
        self.paddle_right.update()
        self.paddle_left.update()

    def _ball_update(self):
        ''' Move the ball and check for collissions with borders and paddles '''
        # Check collission borders
        if self.ball.check_borders():
            self.ball.direction_y *= -1
        
        # Check collission paddles and ball
        self._collission_ball_paddle()

        # Check collissions goals
        self._collission_end_border()

        self.ball.update()

    def _reset(self):
        ''' Reset paddles and the ball '''
        self.paddle_left.reset_paddle()
        self.paddle_right.reset_paddle()
        self.settings.reset_settings()
        self.ball.reset_ball()
        self.ball.direction_x *= 1
        sleep(1) # pauses the game for 1 second

    def _collission_ball_paddle(self):
        ''' Check for collission ball and paddle '''
        # Left paddle and ball collission True of False
        ball_left_paddle_collission = ((self.ball.ball_pos_x <= self.paddle_left.rect.right) and 
            (self.ball.ball_pos_x >= self.paddle_left.rect.left) and 
            (self.ball.ball_pos_y <= self.paddle_left.rect.bottom) and 
            (self.ball.ball_pos_y >= self.paddle_left.rect.top))

        # Right paddle and ball collission True or False
        ball_right_paddle_collission = ((self.ball.ball_pos_x <= self.paddle_right.rect.right) and 
            (self.ball.ball_pos_x >= self.paddle_right.rect.left) and
            (self.ball.ball_pos_y <= self.paddle_right.rect.bottom) and 
            (self.ball.ball_pos_y >= self.paddle_right.rect.top))

        # when ball collides with paddle
        if ball_left_paddle_collission or ball_right_paddle_collission:
            self.ball.direction_x *= -1 # Make the ball go opposite direction
            self.ball.direction_y = self.ball.ball_direction() # Randomize the ball y direction
            self.settings.speedup_ball() # Speedup the game

    def _collission_end_border(self):
        ''' When goal has been scored '''
        left_border = self.ball.ball_pos_x <= 0
        right_border = self.ball.ball_pos_x >= self.settings.screen_width

        # Right player scored
        if left_border:
            self.settings.player_right_score += 1
            self.scoreboard.prep_score_player_right()
            self._reset()
        # Left player scored
        elif right_border:
            self.settings.player_left_score += 1
            self.scoreboard.prep_score_player_left()
            self._reset()

    def _update_screen(self):
        ''' Draw everything to the screen '''
        self.screen.fill(self.settings.bg_color) # background
        self._draw_middle_line()
        self.ball.draw_ball()
        self.paddle_left.draw_paddle()
        self.paddle_right.draw_paddle()
        self.scoreboard.show_score()

        # Draw button if not playing
        if not self.playing:
            self.button.draw_button()
        
        pygame.display.flip() # Refresh screen

    def _draw_middle_line(self):
        ''' Draws the middle line of the play screen '''
        COLOR = self.settings.middle_line_color
        WIDTH = self.settings.middle_line_width

         # Start at mid top screen
        START_POS = (self.settings.screen_width // 2, 0)
         # End at mid bottom screen
        END_POS = (self.settings.screen_width // 2, self.settings.screen_height)

        pygame.draw.line(self.screen, COLOR, START_POS, END_POS, WIDTH)

if __name__ == '__main__':
    pong = Pong()
    pong.main()
