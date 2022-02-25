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

        # 이중 리스트로 화면 경계선(경계선 지나면 나타남)
        self.all_pos_list = [(self.obstacle_width * i, self.obstacle_height * j) for i in range(10) for j in range(10)]
        self.all_pos_list = [self.all_pos_list[i * 10:(i + 1) * 10] for i in range(10)]

        self.pos_list = [(self.obstacle_width * i, 0) for i in range(10)]

        self.initial = True
        self.obstacles = [{
            "pos_x": 0,
            "pos_y": 0,
            "to_y": -6,
            "speed_y": 0,
            "img": pygame.transform.scale(pygame.image.load(os.path.join(self.image_path, "rock1.png")),
                                          (self.obstacle_width, self.obstacle_height)),
            "group": 0  # 총 11가지
        }]
        self.group = 0

    def defineObstaclesRandomPosition(self):
        if self.initial:
            self.num_obstacle = random.randint(0, 10)
            self.real_obstacle_image_list = random.choices(self.obstacle_image_list, k=self.num_obstacle)
            self.real_pos_list = random.sample(self.pos_list, k=self.num_obstacle)
            for image, pos_tuple in zip(self.real_obstacle_image_list,
                                        self.real_pos_list):
                self.obstacles.append({
                    "pos_x": pos_tuple[0],
                    "pos_y": pos_tuple[1],
                    "to_y": -6,
                    "speed_y": 0,
                    "img": image,
                    "group": 0  # 총 11가지
                })
            if self.group == 0:
                del self.obstacles[0]
            self.group += 1

    def blitObstacle(self, screen=None):
        self.defineObstaclesRandomPosition()

        for index, value in enumerate(self.obstacles):
            screen.blit(value["img"], (value["pos_x"], value["pos_y"]))
        self.initial = False

    # def locateObstacle(self):
    #     for obstacle_idx, obstacle_val in enumerate(self.obstacles):
    #         ball_pos_x = obstacle_val["pos_x"]
    #         ball_pos_y = obstacle_val["pos_y"]
    #         ball_img_idx = obstacle_val["img_idx"]
    #
    #         ball_size = ball_images[ball_img_idx].get_rect().size
    #         ball_width = ball_size[0]
    #         ball_height = ball_size[1]
    #
    #         # 가로벽에 닿았을 때 곧 이동 위치 변경(튕겨 나오는 효과)
    #         if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
    #             obstacle_val["to_x"] = obstacle_val["to_x"] * -1
    #
    #         # 세로 위치
    #         if ball_pos_y >= screen_height - stage_height - ball_height:
    #             obstacle_val["to_y"] = obstacle_val["init_spd_y"]
    #         else:  # 그외의 모든 경우에는 속도를 증가
    #             obstacle_val["to_y"] += 0.5
    #
    #         obstacle_val["pos_x"] += obstacle_val["to_x"]
    #         obstacle_val["pos_y"] += obstacle_val["to_y"]
