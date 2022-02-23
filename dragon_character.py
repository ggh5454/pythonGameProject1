import os
import pygame


class Dragon:
    def __init__(self, image_path=None, screen_size=None):
        # 이미지 경로
        self.image_path = image_path

        # 스크린: 크기, 너비, 높이
        self.screen_size = screen_size
        self.screen_width = self.screen_size[0]
        self.screen_height = self.screen_size[1]

        #
        self.dragon_image = pygame.image.load(os.path.join(f"{self.image_path}\\dragon character", "Dragon.png"))
        self.dragon_image = pygame.transform.scale(self.dragon_image, (125, 125))

        self.dragon_size = self.dragon_image.get_rect().size
        self.dragon_width = self.dragon_size[0]
        self.dragon_height = self.dragon_size[1]
        self.dragon_x_pos = (self.screen_width / 2) - (self.dragon_width / 2)
        self.dragon_y_pos = self.screen_height - self.dragon_height
        self.dragon_pos = (self.dragon_x_pos, self.dragon_y_pos)

    def blitDragon(self, screen=None):
        screen.blit(self.dragon_image, self.dragon_pos)
