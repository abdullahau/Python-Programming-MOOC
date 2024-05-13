# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

screen.fill((0, 0, 0))
 
robot = pygame.image.load("robot.png")

class Spawn:
    def __init__(self) -> None:
        self.image = robot
        self.pos_x = randint(0, width - robot.get_width())
        self.pos_y = randint(-100, 0 - robot.get_height())
    
    def move(self):
        if self.pos_y >= height - robot.get_height():
            if self.pos_x > width//2:
                self.pos_x += 1
            else:
                self.pos_x -= 1
        else:
            self.pos_y += 1

class RobotGroup:
    group = [Spawn() for i in range(1,randint(1, 5))]
    
    def __init__(self, number: int):
        if number == 1:
            self.group.append(Spawn())

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    RobotGroup(randint(-50, 50))

    for i in range(0, len(RobotGroup.group)):
        screen.blit(RobotGroup.group[i].image, (RobotGroup.group[i].pos_x, RobotGroup.group[i].pos_y))
        RobotGroup.group[i].move()  
    
    pygame.display.flip()
 
    clock.tick(60)