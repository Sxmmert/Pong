import pygame.font


class ScoreBoard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score_player_left()
        self.prep_score_player_right()

    def prep_score_player_left(self):
        player_left_score_str = str(self.settings.player_left_score)
        self.score_image_player_left = self.font.render(
            player_left_score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect_player_left = self.score_image_player_left.get_rect()
        self.score_rect_player_left.right = (self.settings.screen_width // 2) - 30

    def prep_score_player_right(self):
        player_right_score_str = str(self.settings.player_right_score)
        self.score_image_player_right = self.font.render(
            player_right_score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect_player_right = self.score_image_player_right.get_rect()
        self.score_rect_player_right.left = (self.settings.screen_width // 2) + 30

    def show_score(self):
        self.screen.blit(self.score_image_player_left, self.score_rect_player_left)
        self.screen.blit(self.score_image_player_right, self.score_rect_player_right)
