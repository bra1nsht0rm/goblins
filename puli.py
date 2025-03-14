import pygame
import math
class Bullets:
    def __init__(self, speed, start_x, start_y, enemy, width,height):
        self.speed=speed
        self.x=start_x
        self.y=start_y
        self.enemy=enemy
        self.width=width
        self.height=height
        self.rect=pygame.Rect(self.x, self.y, self.width, self.height)
        #self.image=image
        self.active=True
        if self.enemy:
            goblin_x, goblin_y = self.enemy.get_position()
            print(f"Пуля выпущена из ({self.x}, {self.y}) в гоблина на ({goblin_x}, {goblin_y})")
        else:
            print("Внимание: пуля создана без цели!")


    def update(self,enemy):
        #шаг 1 проверяем наличие цели и активна ли пуля
        if not self.active or not self.enemy:
            print('пуля не активна')
            return False
        else:
            # шаг 2 определяем в какую сторону летит пуля
            goblin_x, goblin_y = self.enemy.get_position()
            # шаг 3 определяем в какуюсторону движется пуля
            if goblin_x>self.x:
                self.x+=5

            elif goblin_x<self.x:
                self.x-=5

            if goblin_y>self.y:
                self.y+=5

            elif goblin_y<self.y:
                self.y-=5

            #шаг 4 обновляем позициию пули
            self.rect.x = self.x
            self.rect.y = self.y

            # шаг 5 проверяем столкновение с врагом
            if self.rect.colliderect(self.enemy.rect):
                self.active = False
                self.enemy.health-=10
                return False

            return True






    def calculate_direction(self):
        if self.enemy:
            goblin_x, goblin_y = self.enemy.get_position()
            dx = goblin_x - self.x  # расстояние от пули до гоблина по x
            dy = goblin_y - self.y  # расстояние от пули до гоблина по y
            bullet_distance = math.sqrt(dx ** 2 + dy ** 2)  # вычесляем радиус - гоблина до пули
            if bullet_distance>0:
                pass






