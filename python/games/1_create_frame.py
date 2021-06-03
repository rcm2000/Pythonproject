import pygame

pygame.init() #필수_ 초기화

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('Ball game')

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x버튼 입력시 QUIT
            running = False

#게임 종료
pygame.quit()