import pygame
import sys
import random
import time
import pygame_menu
import math
pygame.init()
surface = pygame.display.set_mode((700, 700))

class Modeling():
    def __init__(self):
        # задаем размеры экрана
        self.screen_width = 700
        self.screen_height = 700

        # необходимые цвета
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)
        self.light_green = pygame.Color(200, 255, 200)
        self.grey = pygame.Color(128, 128, 128)
        self.blue = pygame.Color(0, 0, 255)

        # Frame per second controller
        # будет задавать количество кадров в секунду
        self.fps_controller = pygame.time.Clock()

        self.number_of_people = NUMBER_OF_PEOPLE

        

    def init_and_check_for_errors(self):
        """Начальная функция для инициализации и
           проверки как запустится pygame"""
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self):
        """Задаем surface(поверхность поверх которой будет все рисоваться)
        и устанавливаем загаловок окна"""
        self.main_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('HELP!')

    def event_loop(self, change_to):
        """Функция для отслеживания нажатий клавиш игроком"""

        # запускаем цикл по ивентам
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

    def refresh_screen(self):
        """обновляем экран и задаем фпс"""
        pygame.display.flip()

    def show_number_of_people(self, choice=1):
        """Отображение количества"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(f'Number of people: {self.number_of_people}', True, self.grey)
        s_rect = s_surf.get_rect()
        # дефолтный случай отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (80, 10)
        # при game_over отображаем результат по центру
        # под надписью game over
        else:
            s_rect.midtop = (360, 120)
        # рисуем прямоугольник поверх surface
        self.main_surface.blit(s_surf, s_rect)
    
    def draw_surface(self):
        self.main_surface.fill(self.light_green)
 
        surf1 = pygame.Surface((500, 400))
        surf1.fill(self.grey)  # серая
        surf2 = pygame.Surface((480, 380))
        surf2.fill(self.white)  # белая

        coords = surf1.get_rect()
        # середина
        midtop = coords.midtop
        surf3 = pygame.Surface((40, 10))
        surf3.fill(self.green) # выход(дверь)

        rect = pygame.Rect((100, 100, 0, 0))
        
        # отрисовка двух прмоугольников
        surf1.blit(surf2, (10, 10))
        surf1.blit(surf3, (midtop[0] - 10, 0))

        # загрузка картинки
        IMG_FIRE = pygame.image.load(r"D:\python\PORJECT_SCHOOL\fire-in-a-room-with-people\fire.png").convert()
        # изменить размеры картинки
        IMG_FIRE = pygame.transform.scale(IMG_FIRE, (60, 60))
        # удалить фон
        IMG_FIRE.set_colorkey((255, 255, 255))

        # огонь
        fire_surf = IMG_FIRE   

        self.main_surface.blit(surf1, rect)
        #отрисовка огня
        self.main_surface.blit(fire_surf, (320, 430)) 

    def the_end(self):
        """конец"""
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('The end', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.main_surface.blit(go_surf, go_rect)
        self.show_number_of_people(0)
        pygame.display.flip()
        time.sleep(3)
        # pygame.quit()
        # sys.exit()

LEFT_BORDER_X = 120
RIGHT_BORDER_X = 580
HIGH_BORDER_Y = 120
LOW_BORDER_Y = 350
L_CENTER = 340
R_CENTER = 360
mini_vector = 20

class Person():
    def __init__(self, person_color):
        # центр человека
        self.person_head_pos = [random.randrange(LEFT_BORDER_X, RIGHT_BORDER_X), random.randrange(HIGH_BORDER_Y, LOW_BORDER_Y)]  # [x, y]

        self.person_color = person_color

        self.direction = "RIGHT"

        # при нажатии соответствующих клавиш
        self.change_to = self.direction

    def validate_direction_and_change(self):
        """Изменияем направление движения человека"""
        # вектор перемещения sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # если левее середины то в левую часть
        if self.person_head_pos[0] < 350:
            vector = math.sqrt((L_CENTER - self.person_head_pos[0]) ** 2 + (HIGH_BORDER_Y - self.person_head_pos[1]) ** 2)
            proec_x = abs(L_CENTER - self.person_head_pos[0])
            proec_y = abs(HIGH_BORDER_Y - self.person_head_pos[1])
            try:
                sin_a = proec_y / vector
                cos_a = proec_x / vector
                del_x = round(cos_a * mini_vector)
                del_y = round(sin_a * mini_vector)
                self.person_head_pos[0] += del_x
                self.person_head_pos[1] -= del_y
            except ZeroDivisionError:
                print(vector)
        # если правее середины то в правую часть
        elif self.person_head_pos[0] > 350:
            try:
                vector = math.sqrt((R_CENTER - self.person_head_pos[0]) ** 2 + (HIGH_BORDER_Y - self.person_head_pos[1]) ** 2)
                proec_x = abs(R_CENTER - self.person_head_pos[0])
                proec_y = abs(HIGH_BORDER_Y - self.person_head_pos[1])
                sin_a = proec_y / vector
                cos_a = proec_x / vector
                del_x = round(cos_a * mini_vector)
                del_y = round(sin_a * mini_vector)
                self.person_head_pos[0] -= del_x
                self.person_head_pos[1] -= del_y
            except ZeroDivisionError:
                print(vector)
        # если ровно посередине
        elif self.person_head_pos[0] == 350:
            self.person_head_pos[1] -= mini_vector

    def get_coords(self):
        """Получаем координаты"""
        pass

    def person_body_mechanism(self, score, food_pos, screen_width, screen_height):
        pass
    

    def draw_person(self, main_surface, surface_color):
        """Отображаем все сегменты человека"""
        # x = random.randrange(120, 580)
        # y = random.randrange(120, 350)
        pygame.draw.circle(main_surface, surface_color, self.person_head_pos, 10)

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        """Проверка границ"""
        pass

 
    
def start_the_modeling():
    modeling = Modeling()

    modeling.init_and_check_for_errors()
    modeling.set_surface_and_title()

    all_people = {}
    people = []
    movements = []
    for i in range(1, NUMBER_OF_PEOPLE + 1):
        person = Person(modeling.blue)
        all_people[f'person{i}'] = person
        people.append()
        
    
    sorted_people = []
    for i in range(1, NUMBER_OF_PEOPLE + 1):

    
    while True:
        modeling.draw_surface()
        for person in all_people.values():        
            person.change_to = modeling.event_loop(person.change_to)

            person.validate_direction_and_change()
            person.change_head_position()
            modeling.show_number_of_people()
            
            # modeling.draw_surface()
            person.draw_person(modeling.main_surface, modeling.blue)

            # person.check_for_boundaries(modeling.the_end, modeling.screen_width, modeling.screen_height)
        modeling.refresh_screen()
        time.sleep(1)



menu = pygame_menu.Menu('Добро пожаловать', 700, 700,
                       theme=pygame_menu.themes.THEME_BLUE)

num_in = menu.add.text_input('Количество людей :', default='10')
NUMBER_OF_PEOPLE = int(num_in.get_value())
menu.add.button('Начать', start_the_modeling)
menu.add.button('Выйти', pygame_menu.events.EXIT)
menu.mainloop(surface)

# import pygame
# import sys
# import random
# pygame.font.init()

# HEIGHT = 700
# WEIGHT = 700
# FPS = 60
# # количество людей  
# NUMBER_OF_PEOPLE = 10

# pygame.init()
# sc = pygame.display.set_mode((HEIGHT, WEIGHT))
# pygame.display.set_caption('HELP!')
# clock = pygame.time.Clock()

# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# GREY = (128, 128, 128) 
# LIGHT_GREEN = (200, 255, 200)

# # загрузка картинки
# IMG_FIRE = pygame.image.load("fire.png").convert()
# # изменить размеры картинки
# IMG_FIRE = pygame.transform.scale(IMG_FIRE, (60, 60))
# # удалить фон
# IMG_FIRE.set_colorkey((255, 255, 255))

# # рисование главно1 области(комнаты)
# def drawing_main_window():
#     # фон
#     sc.fill(LIGHT_GREEN)
 
#     surf1 = pygame.Surface((500, 400))
#     surf1.fill(GREY)  # серая
#     surf2 = pygame.Surface((480, 380))
#     surf2.fill(WHITE)  # белая

#     coords = surf1.get_rect()
#     # середина
#     midtop = coords.midtop
#     surf3 = pygame.Surface((40, 10))
#     surf3.fill(GREEN) # выход(дверь)

#     rect = pygame.Rect((100, 100, 0, 0))
    
#     # отрисовка двух прмоугольников
#     surf1.blit(surf2, (10, 10))
#     surf1.blit(surf3, (midtop[0] - 10, 0))

#     # огонь
#     fire_surf = IMG_FIRE   

#     sc.blit(surf1, rect)
#     #отрисовка огня
#     sc.blit(fire_surf, (320, 430)) 

# # отображение людей
# def draw_people():
#     for i in range(NUMBER_OF_PEOPLE):
#         x = random.randrange(120, 580)
#         y = random.randrange(120, 350)
#         pygame.draw.circle(sc, BLUE, (x, y), 9)

# # отображение количества людей
# def text_people():
#     f1 = pygame.font.Font(None, 36)
#     text1 = f1.render(f'Количество людей: {NUMBER_OF_PEOPLE}', True, RED)
#     sc.blit(text1, (WEIGHT // 2 - 100, HEIGHT - 100))

    
# pygame.display.update()
# c = 0
# while 1:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
    
#     drawing_main_window()
#     if c != 1:
#         draw_people()
#         text_people()
#         pygame.display.update()
#         c += 1
 
#     pygame.time.delay(20)