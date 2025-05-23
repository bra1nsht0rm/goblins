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

    def update(self, enemy=None):
        # шаг 1: проверяем наличие цели и активна ли пуля
        if not self.active or not self.enemy:
            return False

        # шаг 2: вычисляем направление движения пули
        direction_x, direction_y = self.calculate_direction()

        # шаг 3: перемещаем пулю в направлении цели с учетом скорости
        self.x += direction_x * self.speed
        self.y += direction_y * self.speed

        # шаг 4: обновляем позицию пули
        self.rect.x = self.x
        self.rect.y = self.y

        # Отладочная информация
        goblin_x, goblin_y = self.enemy.get_position()
        print(f"Пуля: {self.rect}, Гоблин: {self.enemy.rect}")
        print(f"Расстояние: X={abs(self.x - goblin_x)}, Y={abs(self.y - goblin_y)}")

        # шаг 5: проверяем столкновение с врагом
        if self.rect.colliderect(self.enemy.rect):
            self.active = False
            self.enemy.health -= 10
            print(f"Попадание! Осталось здоровья у гоблина: {self.enemy.health}")
            return False

        # Альтернативная проверка столкновения - проверяем расстояние вручную
        distance = ((self.x - goblin_x)**2 + (self.y - goblin_y)**2) ** 0.5
        if distance < 30:  # если расстояние меньше 30 пикселей, считаем это попаданием
            self.active = False
            self.enemy.health -= 10
            print(f"Попадание (по расстоянию)! Осталось здоровья у гоблина: {self.enemy.health}")
            return False

        return True





    def calculate_direction(self):
        if self.enemy:
            goblin_x, goblin_y = self.enemy.get_position()
            dx = goblin_x - self.x  # расстояние от пули до гоблина по x
            dy = goblin_y - self.y  # расстояние от пули до гоблина по y
            bullet_distance = math.sqrt(dx**2 + dy**2)  # вычисляем расстояние от пули до гоблина

            # Нормализуем вектор направления (создаем единичный вектор)
            if bullet_distance > 0:
                direction_x = dx / bullet_distance
                direction_y = dy / bullet_distance
                return direction_x, direction_y

            return 0, 0  # если расстояние равно 0, возвращаем нулевой вектор






