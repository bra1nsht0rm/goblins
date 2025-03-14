import pygame
import sys
pygame.init()#инициализировали библиотеку pygame
from puli import Bullets
#инициализация - это синхранизация программы и устройства(звук, яркость экрана, микрофон)
import random
# создание экрана
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))  # задаём параметры экрана

# загрузка фона
goblinfon = pygame.image.load("pictes/mainwindow.jpg")
gamefon = pygame.image.load("pictes/pixil-frame.jpg")
goblin_a = pygame.image.load('pictes/frank-a.png')
goblin_b = pygame.image.load('pictes/frank-b.png')
goblin_c = pygame.image.load('pictes/frank-c.png')
goblin_d = pygame.image.load('pictes/frank-d.png')
turel=pygame.image.load('pictes/turel.png')
luk=pygame.image.load('pictes/luk.png')
lives=20
choos_cell=None
selected_cell = None
window_x=0
window_y=0
balance=1000
selection_window_open=False#переменная для проверки открыто окно с выбором или нет
# Цвета
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)

# Шрифт для текста
font = pygame.font.SysFont(None, 55)



#переменные для работы с гоблиннами
goblins = []
initial_x = 1220
initial_y = 455
distance_between_goblins = 320
level = 0
enemies_per_level = 5

class Goblins:
    def __init__(self, image, x, y, speed, damage, health):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.health = health
        self.direction='left'

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self):
        # Двигаемся влево, если x больше 945
        if self.direction == "left":
            if self.x > 945:
                self.x -= self.speed
            else:
                self.direction='up'

        elif self.direction == 'up':
        # Двигаемся вверх, если y больше 112
            if self.y > 113:
                self.y -= self.speed
            else:
                self.direction='left_again'

        elif self.direction == 'left_again':
        # Если x меньше 945, но больше 290, продолжаем движение влево
            if self.x > 289:
                self.x -= self.speed
            else:
                self.direction = 'down'

        elif self.direction=='down':
        # Если y меньше 455, двигаемся вниз
            if self.y < 345:
                self.y += self.speed
            else:
                self.direction='right'

        elif self.direction=='right':
            if self.x<662:
                self.x += self.speed
            else:
                self.direction = 'down_again'

        elif self.direction=='down_again':
            if self.y<548:
                self.y += self.speed
            else:
                self.direction = 'left_again2'

        elif self.direction=='left_again2':
            if self.x>429:
                self.x -= self.speed
            else:
                self.direction = 'up_again'

        elif self.direction=='up_again':
            if self.y>428:
                self.y -= self.speed
            else:
                self.direction = 'left_again3'

        elif self.direction=='left_again3':
            if self.x>178:
                self.x -= self.speed
            else:
                self.direction = 'down_again3'

        elif self.direction=='down_again3':
            if self.y<535:
                self.y += self.speed
            else:
                self.direction = 'right2'

        elif self.direction=='right2':
            if self.x<295:
                self.x += self.speed
            else:
                self.direction = 'down_again4'

        elif self.direction=='down_again4':
            if self.y<585:
                self.y += self.speed
            else:
                self.direction = 'left_again4'

        elif self.direction=='left_again4':
            if self.x>170:
                self.x -= self.speed
            else:
                self.direction = 'down_again5'

        elif self.direction=='down_again5':
            if self.y<720:
                self.y += self.speed

    def check_bounds(self):
        return self.y >= 720

# меод для нахождения центра гоблина
    def get_position(self):
        goblin_center_x=self.x+self.image.get_width()//2
        goblin_center_y=self.y+self.image.get_height()//2
        return goblin_center_x, goblin_center_y






def generate_goblins(level):
    goblinspeed=0.6
    for i in range(enemies_per_level + (level - 1) * 5):

        goblin = Goblins(goblin_a, initial_x + i * distance_between_goblins, initial_y, goblinspeed, 100, 100000)
        goblins.append(goblin)




# Функция параметров текста для кнопок
def draw_text(text, font, color, surface, x, y):
    texti = font.render(text, True, color)  # параметры расположения текста
    textrect = texti.get_rect()  # образует прямоугольник, в котором будет размещён текст
    textrect.topleft = (x, y)  # координаты, по которым будет расположен прямоугольник
    surface.blit(texti, textrect)  # экран, на котором мы расположим прямоугольник и текст



# Функция для создания кнопок
def create_button(x, y, width, height, color, text):
    button = pygame.Rect(x, y, width, height)  # местоположение и размеры кнопки
    pygame.draw.rect(screen, color, button)  # отрисовка прямоугольника
    draw_text(text, font, WHITE, screen, x + 10, y + 10)  # параметры для текста
    return button


# состояние игры
current_screen = "main_menu"

# глобальные переменные для кнопок
button_exit = None
button_start = None
button_exit_game = None
button_next_level = None




def draw_main_menu():
    global button_exit, button_start
    screen.blit(goblinfon, (0, 0))
    button_exit = create_button(1000, 600, 200, 50, RED, 'Выход')
    button_start = create_button(500, 300, 200, 50, GREEN, 'start')
    pygame.display.set_caption('Главное меню')

def draw_next_wave_button():
    global button_next_level
    button_next_level = create_button(500, 150, 200, 50, GREEN, 'Next Wave')

def draw_goblin():
    global lives, goblins
    goblins_to_remove = []
    for goblin in goblins:
        goblin.draw(screen)
        goblin.move()

        if goblin.check_bounds():
            lives-=1
            goblins_to_remove.append(goblin)
    for goblin in goblins_to_remove:
        goblins.remove(goblin)
    draw_text(f"Жизни: {lives}", font, WHITE, screen, 20, 20)



def draw_game_screen():
    global button_exit_game
    screen.blit(gamefon, (0, 0))

    button_exit_game = create_button(1000, 600, 200, 50, RED, 'Выход')
    draw_next_wave_button()  # Отрисовка кнопки для следующей волны
    pygame.display.set_caption("Игровой экран")


def goblin_position():
    goblinN=0

    for temp in goblins:
        goblinN+=1
        temp.get_position()
        #print(goblinN, temp.get_position())







#ЯЧЕЙКИ
grid_cellsx1 = [pygame.Rect(360+50*i,50,40,40)for i in range(13)]
grid_cellsy1 = [pygame.Rect(200,120+50*i,40,40)for i in range(5)]
grid_cellsx2 = [pygame.Rect(500+50*i,220,40,40)for i in range(6)]
grid_cellsy2 = [pygame.Rect(1000,115+50*i,40,40)for i in range(7)]
grid_cellsy3 = [pygame.Rect(730,350+50*i,40,40)for i in range(5)]
grid_cellsx3 = [pygame.Rect(230+50*i,480,40,40)for i in range(4)]
def draw_grid():
    for cell in grid_cellsx1:
        pygame.draw.rect(screen, WHITE, cell, 2)
    for cell in grid_cellsy1:
        pygame.draw.rect(screen, WHITE, cell, 2)
    for cell in grid_cellsx2:
        pygame.draw.rect(screen, WHITE, cell, 2)
    for cell in grid_cellsy2:
        pygame.draw.rect(screen, WHITE, cell, 2)
    for cell in grid_cellsy3:
        pygame.draw.rect(screen, WHITE, cell, 2)
    for cell in grid_cellsx3:
        pygame.draw.rect(screen, WHITE, cell, 2)

class Tureli:
    def __init__(self, price, image, damage, cell):
        self.price=price
        self.turel_image=image
        self.damage=damage
        self.cell=cell
        self.attack_radius=100
    def draw_turel(self,surface):
        surface.blit(self.turel_image,(self.cell.x,self.cell.y))
    def vustrel(self):
        turel_center_x = self.cell.x + self.cell.width // 2
        turel_center_y = self.cell.y + self.cell.height // 2
        return turel_center_x,turel_center_y


    def is_in_radius(self, turel_center_x, turel_center_y, goblin_center_x, goblin_center_y):
        distance=((turel_center_x-goblin_center_x)**2+(turel_center_y-goblin_center_y)**2)**0.5
        #print(distance)
        return distance<=self.attack_radius#если верно возвращает True, иначе False



    def attack_goblin(self, goblins):
        random_x=random.randint(1,1280)
        random_y=random.randint(1,720)
        turel_center_x,turel_center_y = self.vustrel()
        for goblin in goblins:
            goblin_center_x, goblin_center_y = goblin.get_position()
            if self.is_in_radius(turel_center_x, turel_center_y, goblin_center_x, goblin_center_y):
                bullet=Bullets(1,turel_center_x, turel_center_y, goblin, 40, 20)

                list_for_bullet.append(bullet)


                print(list_for_bullet)

                #print(f'гоблин получил урон, осталось {goblin.health}')

                if goblin.health<=0:
                    goblins.remove(goblin)
                break


def update_bullets(list_for_bullets):
    active_bullets=[]
    for temp in list_for_bullets:
        if temp.update:
            active_bullets.append(temp)

    list_for_bullets=active_bullets


def draw_selection_window():
    global window_x, window_y

    window_width=250
    window_hight=60

    window_x=(screen_width-window_width)//2
    window_y=(screen_height-window_hight-90)//2
    pygame.draw.rect(screen,WHITE,(window_x,window_y,window_width,window_hight))

    pygame.draw.rect(screen,GREEN,(window_x+10,window_y+10,40,40))
    screen.blit(turel, (window_x + 12, window_y + 12))

    pygame.draw.rect(screen,RED, (window_x+70,window_y+10,40,40 ))
    screen.blit(luk, (window_x + 72, window_y + 12))



#turel1=Tureli(100,turel,20,(700,723,40,40))
list_for_turel=[]
#print(turel1.cell)
list_for_bullet = []

#def turell_attack():

running = True

while running:





    for event in pygame.event.get():  # Проверка всех событий в игре





        if event.type == pygame.QUIT:  # Если действие - нажатие на кнопку закрытия окна
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левый клик мыши
                if current_screen == 'main_menu' and button_exit.collidepoint(event.pos):  # Проверка, что кликнули по кнопке
                    pygame.quit()
                    sys.exit()
                elif current_screen == 'main_menu' and button_start.collidepoint(event.pos):
                    current_screen = "game_screen"
                    generate_goblins(level)  # Генерация первой волны
                elif current_screen == 'game_screen' and button_exit_game.collidepoint(event.pos):
                    current_screen = "main_menu"
                    lives = 20
                    level = 0
                    goblins.clear()
                elif current_screen == 'game_screen' and button_next_level.collidepoint(event.pos):
                    level += 1
                    generate_goblins(level)  # Генерация новой волны
                elif current_screen == 'game_screen':
                    #for temp in list_for_turel:
                        #if temp.is_in_radius()==True:

                            #print(len(list_for_turel))
                    if selection_window_open and choos_cell:
                        if event.pos[0] >= window_x + 10 and event.pos[0] <= window_x + 50 and event.pos[1] >= window_y + 10 and event.pos[1] <= window_y + 50:
                            selected_icon = "turel"
                            print('Выбрана турель')
                        elif event.pos[0] >= window_x + 70 and event.pos[0] <= window_x + 110 and event.pos[1] >= window_y + 10 and event.pos[1] <= window_y + 50:
                            selected_icon = "luk"
                            print('Выбран лук')
                        # После выбора иконки, создаем объект турели и закрываем окно выбора
                        if selected_icon:
                            if selected_icon == "turel" and balance>=100:
                                new_turel = Tureli(100, turel, 100, choos_cell)
                                list_for_turel.append(new_turel)
                                balance-=100
                            elif selected_icon == "luk" and balance>=100:
                                new_turel = Tureli(100, luk, 100, choos_cell)
                                list_for_turel.append(new_turel)
                                balance -= 100
                            selected_icon = None
                            choos_cell = None
                            selection_window_open = False
                    else:
                        for cell in grid_cellsx1 + grid_cellsy1 + grid_cellsx2 + grid_cellsy2 + grid_cellsx3 + grid_cellsy3:#проходимся по всем ячейкам
                            if cell.collidepoint(event.pos):  # Если мышка была нажата внутри клетки
                                selected_cell = cell  # Переменная, в которой сохраняется объект клетки
                                cell_occupied = False#создаём переменнцю для проверки занята ли клетка или нет
                                for gun in list_for_turel:#создаём цикл для проверки
                                    if selected_cell == gun.cell:#если выбранная ячейка занята
                                        cell_occupied = True#изменяем значение переменной после того как проверяем что клетка занята
                                        print('Клетка занята', selected_cell)
                                        break
                                if not cell_occupied:#проверка изменилось ли значение переменной или нет
                                    choos_cell = selected_cell#сохраним значение координат свободной ячейки
                                    selection_window_open = True#зададим значение переменной для открытия окна с выбором турели
                                    print('Клетка выбрана для размещения турели', selected_cell)
                                else:
                                    choos_cell = None
                                    selection_window_open = False
                                break
                        else:
                            selected_cell = None
                            choos_cell = None
                            selection_window_open = False






    if lives <= 0:  # Проверяем количество жизней ВНУТРИ ИГРОВОГО ЦИКЛА
        current_screen = "main_menu"
        goblins.clear()
        lives = 20
        level = 0
        list_for_turel = []#мы обновляем список что бы при новом запуске игры все ячейки были пустыми
    if current_screen == "main_menu":
        draw_main_menu()
    elif current_screen == "game_screen":
        draw_game_screen()
        coin = draw_text('Баланс: '+ str(balance), font, WHITE, screen, 1000, 20)
        draw_goblin()
        draw_grid()
        goblin_position()




        # Отрисовка турелей на игровом поле
        for turel_obj in list_for_turel:
            turel_obj.draw_turel(screen)

        #for bullet_obj in list_for_bullet:
            #bullet_obj.

        for temp in list_for_turel:
            temp.attack_goblin(goblins)

        for pulya in list_for_bullet:
            pygame.draw.rect(screen,WHITE,pulya)

        # Если окно выбора турели открыто, рисуем его
        if selection_window_open and choos_cell:
            draw_selection_window()
            # Подсвечиваем выбранную клетку
            pygame.draw.rect(screen, GREEN, choos_cell, 2)

    pygame.display.update()  # обновление экрана
