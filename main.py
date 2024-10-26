import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Загрузка иконки и изображения цели
pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/TIR icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

# Начальные координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения цели
target_speed_x = random.choice([-0.15, 0.15])
target_speed_y = random.choice([-0.15, 0.15])

# Цвет фона
color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

# Основной цикл игры
running = True
while running:
    screen.fill(color)

    # Обработка событий#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Отражение цели от стен
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()