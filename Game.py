import pygame
from background import Background
import os
from dragon_character import Dragon, FlameAttack
from obstacle import Obstacle


class Game:
    def __init__(self):
        # 게임 초기화
        pygame.init()

        # screen 설정
        self.screen_size = (1024, 720)  # (가로, 세로)
        self.screen = pygame.display.set_mode(self.screen_size)

        # 화면 타이틀 설정
        pygame.display.set_caption("게임 이름")  # 게임 이름

        # FPS
        self.clock = pygame.time.Clock()

        # 경로
        self.current_path = os.path.dirname(__file__)  # 현재 파일의 경로 반환
        self.image_folder_path = os.path.join(self.current_path, "images")  # image 폴더 위치 반환

        # background.py Background 객체
        self.background = Background(self.image_folder_path, screen_size=self.screen_size)
        # dragon_character.py Dragon 객체
        self.dragonCharacter = Dragon(self.image_folder_path, self.screen_size)
        # obstacle.py Obstacle 객체
        self.obstacle = Obstacle(screen_size=self.screen_size, image_folder_path=self.image_folder_path)
        # dragon_character.py FlameAttack 객체
        self.flame_attack = FlameAttack(image_folder_path=self.image_folder_path, screen_size=self.screen_size)

        # 게임 시작
        Game.startGame(self)

    def startGame(self):
        # 이벤트 루프
        running = True  # 게임이 진행 중인가?
        while running:

            for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                    running = False  # 게임이 진행 중이 아님
                self.dragonCharacter.moveDragonCondition(event=event)
                pygame.event.clear()

            self.background.blitBackground(self.screen, self.screen_size)
            self.dragonCharacter.blitDragon(self.screen, pos=self.dragonCharacter.locateDragon())
            self.obstacle.blitObstacle(self.screen)

            pygame.display.update()  # 게임 화면을 다시 그리기!


if __name__ == "__main__":
    game = Game()
