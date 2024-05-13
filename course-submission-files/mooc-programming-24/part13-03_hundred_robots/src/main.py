# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('robot.png')

window.fill((0, 0, 0))

# Starting position
robot_x = 50
robot_y = 100

counter = 0
x_offset = 0
while counter < 100:
    for i in range(0, 10):
        robot_x += 40
        window.blit(robot, (robot_x, robot_y))
    robot_y += 20
    x_offset += 10
    robot_x = 50 + x_offset
    counter += 10
    
        
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()