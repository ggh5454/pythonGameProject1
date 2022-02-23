import os
import pygame
import random


class Obstacle:
    def __init__(self, screen_size=None, image_folder_path=None):
        # 크기 설정
        self.num_obstacle = 0
        self.obstacle_width = screen_size[0] // 10  # 화면 가로 10개
        self.obstacle_height = screen_size[1] // 10  # 화면 세로 10개

        # 여러 장애물 이미지 로드
        self.obstacle_image = []
        self.image_path = f"{image_folder_path}\\rocks"  # 폴더
        for path in os.listdir(self.image_path):  # 파일 경로
            obstacle_image = pygame.image.load(os.path.join(self.image_path, path))  # 이미지 불러오기
            obstacle_image = pygame.transform.scale(obstacle_image,
                                                    (self.obstacle_width, self.obstacle_height))  # 이미지 스케일 조정
            self.obstacle_image.append(obstacle_image)

        del self.obstacle_image[5]

        self.obstacle_pos = (20, 20)

    def blitObstacle(self, screen=None, pos=None):
        screen.blit(self.obstacle_image[0], self.obstacle_pos if pos is None else pos)
