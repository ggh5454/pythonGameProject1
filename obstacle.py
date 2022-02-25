import os
import pygame
import random


class Obstacle:
    def __init__(self, screen_size=None, image_folder_path=None):
        # 크기 설정
        self.screen_size = screen_size
        self.obstacle_width = self.screen_size[0] // 10  # 화면 가로 10개
        self.obstacle_height = self.screen_size[1] // 10  # 화면 세로 10개

        # 여러 장애물 이미지 로드
        self.obstacle_image_list = []
        self.image_path = f"{image_folder_path}\\rocks"  # 폴더
        for path in os.listdir(self.image_path):  # 파일 경로
            obstacle_image = pygame.image.load(os.path.join(self.image_path, path))  # 이미지 불러오기
            obstacle_image = pygame.transform.scale(obstacle_image,
                                                    (self.obstacle_width, self.obstacle_height))  # 이미지 스케일 조정
            self.obstacle_image_list.append(obstacle_image)

        # 화면 경계선(경계선 지나면 새로운 장애물 나타남)
        self.all_pos_list = [self.obstacle_height * j for j in range(0, 10)]

        # 첫 번쨰 장애물 그룹의 위치
        self.pos_list = [(self.obstacle_width * i, -self.obstacle_height) for i in range(10)]
        self.obstacles = [{
            "pos_x": 0,
            "pos_y": 0,
            "speed_y": 0.1,
            "img": pygame.transform.scale(pygame.image.load(os.path.join(self.image_path, "rock1.png")),
                                          (self.obstacle_width, self.obstacle_height)),
            "group": 0  # 총 11가지
        }]
        del self.obstacles[0]
        self.group = 0  # 그룹

        self.can_be_created = True

    def defineObstaclesRandomPosition(self):
        if self.can_be_created:
            self.num_obstacle = random.randint(0, 9)  # 한 줄에 어느 정도 장애물을 만들 것이냐?
            self.real_obstacle_image_list = random.choices(self.obstacle_image_list,
                                                           k=self.num_obstacle)  # 랜덤 숫자대로 이미지를 고르기
            self.real_pos_list = random.sample(self.pos_list, k=self.num_obstacle)  # 랜덤 숫자대로 이미지 위치 고르기
            for image, pos_tuple in zip(self.real_obstacle_image_list,
                                        self.real_pos_list):
                self.obstacles.append({
                    "pos_x": pos_tuple[0],
                    "pos_y": pos_tuple[1],
                    "speed_y": 1,
                    "img": image,
                    "group": self.group  # 총 11가지
                })

            self.group += 1
            self.can_be_created = False

    def blitObstacle(self, screen=None):
        self.defineObstaclesRandomPosition()
        self.locateObstacle(screen_height=self.screen_size[1])
        for index, value in enumerate(self.obstacles):
            screen.blit(value["img"], (value["pos_x"], value["pos_y"]))

    def locateObstacle(self, screen_height=None):
        for obstacle_idx, obstacle_val in enumerate(self.obstacles):
            obstacle_pos_y = obstacle_val["pos_y"]
            # 세로 위치
            if obstacle_pos_y >= screen_height:
                del self.obstacles[obstacle_idx]

            obstacle_val["pos_y"] += obstacle_val["speed_y"]

            if obstacle_pos_y in self.all_pos_list and obstacle_idx == len(self.obstacles) - 1:
                self.can_be_created = True
                self.defineObstaclesRandomPosition()
