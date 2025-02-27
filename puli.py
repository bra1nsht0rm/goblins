import pygame
class Bullets:
    def __init__(self, speed, start_x, start_y, enemy, width,height):
        self.speed=speed
        self.start_x=start_x
        self.start_y=start_y
        self.enemy=enemy
        self.width=width
        self.height=height
        self.rect=pygame.Rect(self.start_x, self.start_y, self.width, self.height)
        #self.image=image

    def shot(self,enemy):
        goblin_x, goblin_y = self.enemy.get_position()
        dx=goblin_x - self.x# расстояние от пули до гоблина по x
        dy=goblin_y - self.y# расстояние от пули до гоблина по y
        bullet_distance=(dx**2 + dy**2)**0.5#вычесляем радиус - гоблина до пули

        print('good')


