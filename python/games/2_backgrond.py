import pygame

pygame.init() #필수_ 초기화

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('Ball game')

# 배경이미지 불러오기
background = pygame.image.load('C:\\PycharmProjects\\games\\background.png')

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x버튼 입력시 QUIT
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    #screen.fill((0,0,255)) #배경 RGB로 채우기
    pygame.display.update() #게임화면 계속 그리기
#게임 종료
pygame.quit()