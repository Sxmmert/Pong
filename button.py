import pygame.font
import pygame


class Button:
    ''' class for the start button '''
    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Button settings
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Places the button in the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        ''' Makes the message ready for drawing it to the screen '''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center
    
    def draw_button(self):
        ''' Draw button to screen '''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
