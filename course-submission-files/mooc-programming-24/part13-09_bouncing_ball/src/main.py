# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")

clock = pygame.time.Clock()

x = randint(5, width - ball.get_width())
y = randint(5, height - ball.get_height())
x_direction = 1
y_direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    if x == 0 or x == width - ball.get_width():
        x_direction = -x_direction
    
    if y == 0 or y == height - ball.get_height():
        y_direction = -y_direction
    
    x += x_direction
    y += y_direction
    
    window.blit(ball, (x, y))
    
    pygame.display.flip()

    clock.tick(80)