# WRITE YOUR SOLUTION HERE:
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

robot1 = pygame.image.load("robot.png")
x1 = width - robot_width/2
y1 = height - robot_width/2

to_right_r1 = False
to_left_r1 = False
to_up_r1 = False
to_down_r1 = False

robot2 = pygame.image.load("robot.png")
x2 = 0
y2 = 0

to_right_r2 = False
to_left_r2 = False
to_up_r2 = False
to_down_r2 = False

clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left_r1 = True
            if event.key == pygame.K_RIGHT:
                to_right_r1 = True
            if event.key == pygame.K_UP:
                to_up_r1 = True
            if event.key == pygame.K_DOWN:
                to_down_r1 = True
            if event.key == pygame.K_a:
                to_left_r2 = True
            if event.key == pygame.K_d:
                to_right_r2 = True
            if event.key == pygame.K_w:
                to_up_r2 = True
            if event.key == pygame.K_s:
                to_down_r2 = True
            
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left_r1 = False
            if event.key == pygame.K_RIGHT:
                to_right_r1 = False
            if event.key == pygame.K_UP:
                to_up_r1 = False
            if event.key == pygame.K_DOWN:
                to_down_r1 = False
            if event.key == pygame.K_a:
                to_left_r2 = False
            if event.key == pygame.K_d:
                to_right_r2 = False
            if event.key == pygame.K_w:
                to_up_r2 = False
            if event.key == pygame.K_s:
                to_down_r2 = False
 
        if event.type == pygame.QUIT:
            exit()
 
    if to_right_r1:
        x1 += 2
    if to_left_r1:
        x1 -= 2
    if to_up_r1:
        y1 -= 2
    if to_down_r1:
        y1 += 2

    if to_right_r2:
        x2 += 2
    if to_left_r2:
        x2 -= 2
    if to_up_r2:
        y2 -= 2
    if to_down_r2:
        y2 += 2
 
    x1 = max(x1,0)
    x1 = min(x1,width - robot_width)
    y1 = max(y1,0)
    y1 = min(y1,height - robot_height)
    
    x2 = max(x2,0)
    x2 = min(x2,width - robot_width)
    y2 = max(y2,0)
    y2 = min(y2,height - robot_height)    
 
    screen.fill((0, 0, 0))
    
    screen.blit(robot1, (x1, y1))
    
    screen.blit(robot2, (x2, y2))
    
    pygame.display.flip()
 
    clock.tick(60)