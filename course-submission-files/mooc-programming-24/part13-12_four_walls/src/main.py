# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
x = (width-robot.get_width())/2
y = (height-robot.get_height())/2

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x <= width - robot.get_width() - 2:
        x += 2
    if to_left and x >= 0 + 2:
        x -= 2
    if to_up and y > 0 + 2:
        y -= 2
    if to_down and y < height - robot.get_height() - 2:
        y += 2
         
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)