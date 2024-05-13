# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

top_x = 0
bottom_x = 640 - robot.get_width()
y = 50
top_velocity = 1
bottom_velocity = -2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (top_x, y))
    window.blit(robot, (bottom_x, y+100))
    pygame.display.flip()
    
    top_x += top_velocity
    
    if top_velocity > 0 and top_x+robot.get_width() >= 640:
        top_velocity = -top_velocity
    if top_velocity < 0 and top_x <= 0:
        top_velocity = -top_velocity

    bottom_x += bottom_velocity
    
    if bottom_velocity > 0 and bottom_x+robot.get_width() >= 640:
        bottom_velocity = -bottom_velocity
    if bottom_velocity < 0 and bottom_x <= 0:
        bottom_velocity = -bottom_velocity        
    

    clock.tick(60)