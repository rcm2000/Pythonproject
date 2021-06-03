import pygame

pygame.init() #필수_ 초기화

# 화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('Ball game')

# 배경이미지 불러오기
background = pygame.image.load('C:\\PycharmProjects\\games\\background.png')


# 캐릭터 불러오기
character = pygame.image.load('C:\\PycharmProjects\\games\\charactor.png')
character_size = character.get_rect().size #이미지 크기 구해오기
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = screen_width / 2 - character_size[0]/2 # 화면 가로의 절반 _ 정가운데 위치
character_y_pos = screen_height - character_size[1] - 48 #화면 세로 가장 아래
# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x버튼 입력시 QUIT
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    #screen.fill((0,0,255)) #배경 RGB로 채우기
    pygame.display.update() #게임화면 계속 그리기
#게임 종료
pygame.quit()