import pygame
from sys import exit
from constants import WHITE, WIDTH, HEIGHT, FPS
from snake import Snake

pygame.init()
pygame.display.set_caption("Snake")
key_pressed = pygame.key.get_pressed()
clock = pygame.time.Clock()

snake = Snake()
is_game_on = True

while is_game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                snake.up()
            elif event.key == pygame.K_LEFT:
                snake.left()
            elif event.key == pygame.K_DOWN:
                snake.down()
            elif event.key == pygame.K_RIGHT:
                snake.right()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.draw.rect(WINDOW, WHITE, snake)
    snake.move()
    pygame.display.update()
    clock.tick(FPS)
