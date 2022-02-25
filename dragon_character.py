import os
import pygame


class Dragon:
    def __init__(self, image_folder_path=None, screen_size=None):
        # 이미지 경로
        self.image_folder_path = image_folder_path

        # 스크린: 크기, 너비, 높이
        self.screen_size = screen_size
        self.screen_width = self.screen_size[0]
        self.screen_height = self.screen_size[1]

        # dragon 이미지 불러오기, 스케일 조정
        self.dragon_image = pygame.image.load(os.path.join(f"{self.image_folder_path}\\dragon character", "Dragon.png"))
        self.dragon_image = pygame.transform.scale(self.dragon_image, (125, 125))

        # 사이즈, 너비, 높이, x위치, y 위치
        self.dragon_size = self.dragon_image.get_rect().size
        self.dragon_width = self.dragon_size[0]
        self.dragon_height = self.dragon_size[1]
        self.dragon_x_pos = (self.screen_width / 2) - (self.dragon_width / 2)
        self.dragon_y_pos = self.screen_height - self.dragon_height
        self.dragon_pos = (self.dragon_x_pos, self.dragon_y_pos)

        # dragon 이동 방향
        self.dragon_to_left = 0  # 왼쪽
        self.dragon_to_right = 0  # 오른쪽
        self.dragon_to_top = 0  # 위쪽
        self.dragon_to_bottom = 0  # 아래쪽

        # dragon 이동 속도
        self.dragon_speed = 5



    def blitDragon(self, screen=None, pos=None):
        # 드래곤 그리기
        screen.blit(self.dragon_image, self.dragon_pos if pos is None else pos)

    def moveDragonCondition(self, event=None):
        # 누르면
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 캐릭터 왼쪽으로
                self.dragon_to_left -= self.dragon_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                self.dragon_to_right += self.dragon_speed
            elif event.key == pygame.K_UP:  # 캐릭터 위쪽으로
                self.dragon_to_top -= self.dragon_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터 아래쪽으로
                self.dragon_to_bottom += self.dragon_speed

        # 키보드 누르고 뗐을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  # 캐릭터 왼쪽으로
                self.dragon_to_left = 0
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                self.dragon_to_right = 0
            elif event.key == pygame.K_UP:  # 캐릭터 위쪽으로
                self.dragon_to_top = 0
            elif event.key == pygame.K_DOWN:  # 캐릭터 아래쪽으로
                self.dragon_to_bottom = 0

    def locateDragon(self):
        # 위치 정의
        self.dragon_x_pos += self.dragon_to_left + self.dragon_to_right
        self.dragon_y_pos += self.dragon_to_top + self.dragon_to_bottom

        # 세로 경계값 처리
        if self.dragon_x_pos < 0:
            self.dragon_x_pos = 0
        elif self.dragon_x_pos > self.screen_width - self.dragon_width:
            self.dragon_x_pos = self.screen_width - self.dragon_width

        # 가로 경계값 처리
        if self.dragon_y_pos < 0:
            self.dragon_y_pos = 0
        elif self.dragon_y_pos > self.screen_height - self.dragon_height:
            self.dragon_y_pos = self.screen_height - self.dragon_height

        self.dragon_pos = (self.dragon_x_pos, self.dragon_y_pos)

        return self.dragon_pos


class FlameAttack(Dragon):
    def __init__(self, image_folder_path=None, screen_size=None):
        super().__init__(image_folder_path, screen_size)

        self.screen_width = self.screen_size[0]
        self.screen_height = self.screen_size[1]

        # 여러 불꽃 이미지 로드
        self.flame_image_list, temp_flame_image_list = [], []  # 이미지 경로 저장을 위한 변수들
        self.flame_size = (40, 60)  # 불꽃 사이즈
        self.image_path = f"{self.image_folder_path}\\fire"  # 폴더
        for path in os.listdir(self.image_path):  # 파일 경로
            flame_image = pygame.image.load(os.path.join(self.image_path, path))  # 이미지 불러오기
            flame_image = pygame.transform.scale(flame_image, self.flame_size)  # 이미지 스케일 조정
            if path.find('5') or path.find('0'):  # 0이나 5가 포함될 경우 list 통째로 저장, 5번째 씩 이미지 짝이 맞아서
                self.flame_image_list.append(temp_flame_image_list)
            else:  # 아닐 경우 저장
                temp_flame_image_list.append(flame_image)

        # 불꽃 사이즈, 너비, 높이, x위치, y 위치
        self.flame_width = self.flame_size[0]
        self.flame_height = self.flame_size[1]
        self.flame_x_pos = (self.screen_width / 2) + (self.dragon_width / 2) - (self.flame_width / 2)
        self.flame_y_pos = self.screen_height - self.dragon_height
        self.flame_pos = (self.flame_x_pos, self.flame_y_pos)

        # 불꽃 이동 속도 (위쪽으로)
        self.flame_speed_to_y = - 5
