import os
import pygame
import random


class Obstacle:
    def __init__(self, screen_size=None, image_folder_path=None):
        # 크기 설정
        self.obstacle_width = screen_size[0] // 10  # 화면 가로 10개
        self.obstacle_height = screen_size[1] // 10  # 화면 세로 10개

        # 여러 장애물 이미지 로드
        self.obstacle_image_list = []
        self.image_path = f"{image_folder_path}\\rocks"  # 폴더
        for path in os.listdir(self.image_path):  # 파일 경로
            obstacle_image = pygame.image.load(os.path.join(self.image_path, path))  # 이미지 불러오기
            obstacle_image = pygame.transform.scale(obstacle_image,
                                                    (self.obstacle_width, self.obstacle_height))  # 이미지 스케일 조정
            self.obstacle_image_list.append(obstacle_image)

        self.all_pos_list = [(self.obstacle_width * i, self.obstacle_height * j) for i in range(10) for j in range(10)]
        self.pos_list = [(self.obstacle_width * i, 0) for i in range(10)]

        self.obstacle_pos = (20, 20)
        self.a = True

    def blitObstacle(self, screen=None):
        if self.a:
            self.num_obstacle = random.randint(0, 10)
            self.real_obstacle_image_list = random.choices(self.obstacle_image_list, k=self.num_obstacle)
            self.real_pos_list = random.sample(self.pos_list, k=self.num_obstacle)
        for index, pos in enumerate(self.real_pos_list):

            screen.blit(self.real_obstacle_image_list[index], pos)
        self.a = False
