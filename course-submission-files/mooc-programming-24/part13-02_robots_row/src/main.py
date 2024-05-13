# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window_x, window_y = 640, 480
window = pygame.display.set_mode((window_x, window_y))

robot = pygame.image.load('robot.png')

window.fill((0, 0, 0))

robot_width = robot.get_width()

# Starting position
robot_x = 50
robot_y = 100

window.blit(robot, (robot_x, robot_y))

for i in range(1, 10):
    robot_x += robot_width
    window.blit(robot, (robot_x, robot_y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()