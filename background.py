import os
import pygame


class Background:
    def __init__(self, image_path=None, screen_size=None):
        # 스크린 크기, 이미지 경로
        self.screen_size = screen_size
        self.image_path = image_path

        # 배경 만들기
        self.background_image = pygame.image.load(
            os.path.join(f"{self.image_path}\\background\Battleground1\Bright", "Battleground1.png"))
        self.background_image = pygame.transform.scale(self.background_image, self.screen_size)  # 배경 크기에 맞게 이미지 크기 조절

    def blitBackground(self, screen, screen_size):
        screen.blit(pygame.transform.scale(self.background_image, screen_size), (0, 0))  # 배경 그리기


if __name__ == "__main__":
    background = Background()
