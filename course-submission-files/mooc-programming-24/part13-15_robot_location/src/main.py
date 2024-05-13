# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint, choice
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

robot_pos = (randint(0, width - robot_width), randint(0, height - robot_height))

def robot_range(robot_pos: tuple):
    min_x = robot_pos[0]
    max_x = robot_pos[0] + robot_width
    min_y = robot_pos[1]
    max_y = robot_pos[1] + robot_height
    return [list(range(min_x, max_x)), list(range(min_y, max_y))]

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pip = robot_range(robot_pos)
            if event.pos[0] in pip[0] and event.pos[1] in pip[1]:
                x_cord = choice([i for i in range(0, width - robot_width) if i not in pip[0]])
                y_cord = choice([i for i in range(0, height - robot_height) if i not in pip[1]])
                robot_pos = (x_cord, y_cord)
 
        if event.type == pygame.QUIT:
            exit()
    
    screen.fill((0, 0, 0))
    screen.blit(robot, robot_pos)
    pygame.display.flip()