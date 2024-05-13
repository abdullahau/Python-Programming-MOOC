# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

radius = 130
center_x = 640/2
center_y = 480/2
angle = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    for i in range(10):
        rad = angle + (i * (2 * math.pi)/10)
        x = center_x + math.cos(rad) * radius - robot.get_width()/2
        y = center_y + math.sin(rad) * radius - robot.get_height()/2
        window.blit(robot, (x, y))
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)