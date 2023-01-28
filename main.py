import pygame
import sys
import random
import time
import pygame_menu
import math
pygame.init()
surface = pygame.display.set_mode((700, 700))

class Modeling():
    def __init__(self, number=10):
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

        self.number_of_people = number

        

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
        s_surf = s_font.render(f'Количество человек: {self.number_of_people}', True, self.blue)
        s_rect = s_surf.get_rect()
        # дефолтный случай отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (100, 40)
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
# в будущем для бодьщей шибкости и вариативности
# Length = 460
# High = 230

LEFT_BORDER_X = 120
RIGHT_BORDER_X = 580
HIGH_BORDER_Y = 120
LOW_BORDER_Y = 480
L_CENTER = 340
R_CENTER = 360
MIDDLE = 350
mini_vector = 20

class Person():
    def __init__(self, person_color):
        # центр человека
        self.person_head_pos = [random.randrange(LEFT_BORDER_X + 10, RIGHT_BORDER_X - 10), random.randrange(HIGH_BORDER_Y + 10, LOW_BORDER_Y - 10)]  # [x, y]

        self.person_color = person_color

        self.direction = "OK"

        # при нажатии соответствующих клавиш
        self.change_to = self.direction

    def validate_direction_and_change(self):
        """Изменияем направление движения человека"""
        # вектор перемещения sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # если левее середины то в левую часть
        if self.person_head_pos[0] < 340:
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
        # если в центре
        elif 340 <= self.person_head_pos[0] <= 360:
            self.person_head_pos[1] -= mini_vector
        # если правее середины то в правую часть
        elif self.person_head_pos[0] > 360:
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

    def get_coords(self):
        """Получаем координаты"""
        return (self.person_head_pos[0], self.person_head_pos[1])

    def get_vector_to_exit(self):
        """Получаем длину вектор до выхода"""
        vector = math.sqrt((MIDDLE - self.person_head_pos[0]) ** 2 + (MIDDLE- self.person_head_pos[1]) ** 2)
        return vector

    def person_body_mechanism(self, score, screen_width, screen_height):
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
    NUMBER_OF_PEOPLE = int(num_in.get_value())
    modeling = Modeling(NUMBER_OF_PEOPLE)

    modeling.init_and_check_for_errors()
    modeling.set_surface_and_title()
    
    all_people = {}   
    # для заполнения помещения
    k = NUMBER_OF_PEOPLE
    i = 0
    # список кортежей, где не может появится человек
    invalid_coordinates = []
    while k > 0:
        person = Person(modeling.blue)
        x_cut, y_cut = person.get_coords()

        def check_coors(x, y):
            for j in range(i):
                print(j)
                print(invalid_coordinates)
                if ((invalid_coordinates[j][0] <= x <= invalid_coordinates[j][1])
                    and (invalid_coordinates[j][2] <= y <= invalid_coordinates[j][3])):
                    return False
            return True

        if i == 0:
            all_people[f'person{i}'] = person
            invalid_coordinates.append((x_cut - 20, x_cut + 20, y_cut - 20, y_cut + 2))
            print(invalid_coordinates)            
            k -= 1
            i += 1
            print(i)
        elif check_coors(x_cut, y_cut):
            all_people[f'person{i}'] = person
            invalid_coordinates.append((x_cut - 20, x_cut + 20, y_cut - 20, y_cut + 20))
            print(invalid_coordinates)             
            k -= 1
            i += 1
            print(i)
        else:
            # удалить экземпляр класса
            del person       

    # создаем список словарей
    sorted_people = []
    for item in all_people.values():
        sorted_people.append({'person': item,
                             'vector_to_exit': item.get_vector_to_exit(),
                             'color': item.person_color})
    # сортируем списовк слловарей, чтобы в главном цикле начинать с ближайшего
    sorted_people.sort(key=lambda dictionary: dictionary['vector_to_exit'])
    print(sorted_people)
    
    while True:
        modeling.draw_surface()
        for dic in sorted_people:
            person = dic['person']        
            person.change_to = modeling.event_loop(person.change_to)

            person.validate_direction_and_change()
            modeling.show_number_of_people()
            
            # modeling.draw_surface()
            person.draw_person(modeling.main_surface, modeling.blue)

            # person.check_for_boundaries(modeling.the_end, modeling.screen_width, modeling.screen_height)
        modeling.refresh_screen()
        time.sleep(1)



menu = pygame_menu.Menu('Добро пожаловать', 700, 700,
                       theme=pygame_menu.themes.THEME_BLUE)

num_in = menu.add.text_input('Количество людей :', default='10')
# NUMBER_OF_PEOPLE = int(num_in.get_value())
# print(NUMBER_OF_PEOPLE)
# print(num_in)
menu.add.button('Начать', start_the_modeling)
menu.add.button('Выйти', pygame_menu.events.EXIT)
menu.mainloop(surface)
