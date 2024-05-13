# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

x = 0
y = 0
horizontal_velocity = 1
vertical_velocity = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += horizontal_velocity
    y += vertical_velocity
    
    # upper left to upper right
    if horizontal_velocity > 0 and x + robot.get_width() >= width:
        horizontal_velocity = 0
        vertical_velocity = 1
    
    # upper right to lower right
    if vertical_velocity > 0 and y + robot.get_height() >= height:
        horizontal_velocity = -1
        vertical_velocity = 0
    
    # lower right to lower left
    if horizontal_velocity < 0 and x <= 0:
        horizontal_velocity = 0
        vertical_velocity = - 1
    
    # lower left to upper let
    if vertical_velocity < 0 and y <= 0:
        horizontal_velocity = 1
        vertical_velocity = 0 

    clock.tick(60)