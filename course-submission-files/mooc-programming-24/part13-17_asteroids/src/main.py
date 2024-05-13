# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Asteroids")

# Robot object, starting position and controls
robot = pygame.image.load("robot.png")
x = 0
y = height - robot.get_height()

controls = [(pygame.K_LEFT, -2), (pygame.K_RIGHT, 2)]

# Robot Range 
def robot_range(min_x: int):
    return set(((x, y) for x in range(min_x, min_x + robot.get_width()+1) 
                for y in range(height - robot.get_height(), height+1)))

# Rock & Rock Range
rock = pygame.image.load("rock.png")
number = 5
rocks = [[-1000, height] for i in range(number)]

def rock_range(rock_pos: list):
    return set(((x, y) for x in range(rock_pos[0], rock_pos[0] + rock.get_width()+1) 
                for y in range(rock_pos[1], rock_pos[1] + rock.get_height()+1)))

# Score font object
game_font = pygame.font.SysFont("Arial", 24)
point = 0

clock = pygame.time.Clock()

key_pressed = {}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
             key_pressed[event.key] = True
            
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]

    for key in controls:
        button, mov_x = key
        if button in key_pressed:
            x += mov_x

    for i in range(number):
        if rocks[i][1] + rock.get_height() < height:
            # the rock falls downwards
            rocks[i][1] += 1
        elif rocks[i][0] < -rock.get_width():
            # new random start point
            rocks[i][0] = randint(0,width-rock.get_width())
            rocks[i][1] = -randint(200,2000)
        else:
            exit()
    
    screen.fill((0, 0, 0))
    
    # Rock Display
    for i in range(number):
        robot_space = robot_range(x)
        rock_space = rock_range(rocks[i])
        if rock_space.intersection(robot_space):
            rocks[i] = [-1000, height]
            point += 1
        else:
            screen.blit(rock, (rocks[i][0], rocks[i][1]))    

    # Robot Display
    screen.blit(robot, (x, y))
    
    # Score Display
    score = game_font.render(f"Points: {point}", True, (255, 0, 0))
    screen.blit(score, (width - score.get_width() - 20, 10))
 
    pygame.display.flip()
    
    clock.tick(60)