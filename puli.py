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
        self.rect=pygame.Rect(self.start_x, self.start_y, self.width, self.height)
        #self.image=image
        self.active=True
        self.dx=0
        self.dy=0

    def shot(self,enemy):
        if self.enemy:
            goblin_x, goblin_y = self.enemy.get_position()
            if goblin_x>self.start_x:
                self.start_x+=5
                if self.rect.colliderect(self.enemy):
                    self.active=False
            elif goblin_x<self.start_x:
                self.start_x-=5
                if self.rect.colliderect(self.enemy):
                    self.active=False
            if goblin_y>self.start_y:
                self.start_y+=5
                if self.rect.colliderect(self.enemy):
                    self.active=False
            elif goblin_y<self.start_y:
                self.start_y-=5
                if self.rect.colliderect(self.enemy):
                    self.active=False







    def calculate_direction(self):
        if self.enemy:
            goblin_x, goblin_y = self.enemy.get_position()
            dx = goblin_x - self.x  # расстояние от пули до гоблина по x
            dy = goblin_y - self.y  # расстояние от пули до гоблина по y
            bullet_distance = math.sqrt(dx ** 2 + dy ** 2)  # вычесляем радиус - гоблина до пули
            if bullet_distance>0:






