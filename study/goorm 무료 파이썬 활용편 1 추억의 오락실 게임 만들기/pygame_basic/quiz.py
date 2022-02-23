import pygame
import random

###################################################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로
screen_height = 640  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")  # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 캐릭터, 폰트 등)
# 배경 민들기
background = pygame.image.load("raw/backgroundImage1.png")

# 캐릭터 만들기 (load, size, width, height, x_pos, y_pos, 이동 위치, 이동 속도)
character = pygame.image.load("raw/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_x = 0
character_speed = 0.6

# 똥 만들기 (load, size, width, height, x_pos, y_pos, 이동 위치, 이동 속도)
ddong = pygame.image.load("raw/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_y = 0
ddong_speed = 5

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                character_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                character_x += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_x = 0

    character_x_pos += character_x * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # 충돌 체크
    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))  # 적 그리기
    pygame.display.update()
    ddong_y_pos += ddong_speed

# pygame 종료
pygame.quit()
