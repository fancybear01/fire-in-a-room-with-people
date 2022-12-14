import pygame
import sys
import random
pygame.font.init()

HEIGHT = 700
WEIGHT = 700
FPS = 60
# количество людей  
NUMBER_OF_PEOPLE = 10

pygame.init()
sc = pygame.display.set_mode((HEIGHT, WEIGHT))
pygame.display.set_caption('HELP!')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128) 
LIGHT_GREEN = (200, 255, 200)

# загрузка картинки
IMG_FIRE = pygame.image.load("fire.png").convert()
# изменить размеры картинки
IMG_FIRE = pygame.transform.scale(IMG_FIRE, (60, 60))
# удалить фон
IMG_FIRE.set_colorkey((255, 255, 255))

# рисование главно1 области(комнаты)
def drawing_main_window():
    # фон
    sc.fill(LIGHT_GREEN)
 
    surf1 = pygame.Surface((500, 400))
    surf1.fill(GREY)  # серая
    surf2 = pygame.Surface((480, 380))
    surf2.fill(WHITE)  # белая

    coords = surf1.get_rect()
    # середина
    midtop = coords.midtop
    surf3 = pygame.Surface((40, 10))
    surf3.fill(GREEN) # выход(дверь)

    rect = pygame.Rect((100, 100, 0, 0))
    
    # отрисовка двух прмоугольников
    surf1.blit(surf2, (10, 10))
    surf1.blit(surf3, (midtop[0] - 10, 0))

    # огонь
    fire_surf = IMG_FIRE   

    sc.blit(surf1, rect)
    #отрисовка огня
    sc.blit(fire_surf, (320, 430)) 

# отображение людей
def draw_people():
    for i in range(NUMBER_OF_PEOPLE):
        x = random.randrange(120, 580)
        y = random.randrange(120, 350)
        pygame.draw.circle(sc, BLUE, (x, y), 9)

# отображение количества людей
def text_people():
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(f'Количество людей: {NUMBER_OF_PEOPLE}', True, RED)
    sc.blit(text1, (WEIGHT // 2 - 100, HEIGHT - 100))

    
pygame.display.update()
c = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    
    drawing_main_window()
    if c != 1:
        draw_people()
        text_people()
        pygame.display.update()
        c += 1
 
    pygame.time.delay(20)