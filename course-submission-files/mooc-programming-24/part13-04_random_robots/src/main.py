# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))

right_x_limit = 640 - robot.get_width()
down_y_limit = 480 - robot.get_height()

for i in range(1000):
    screen.blit(robot, (randint(0 , right_x_limit), randint(0, down_y_limit)))
        
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()