# More pygame techniques

# The window title

# Your programs will look more professional if instead of "pygame window" the window title contains the actual name of the program.
# The title is set with the `pygame.display.set_caption` function:

pygame.display.set_caption("Great Adventure")

# Drawing shapes

# The following program draws a rectangle, a circle and a line on the screen:

import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# rect(surface, color, rect) -> Rect
pygame.draw.rect(display, (0, 255, 0), (50, 100, 200, 250))

# circle(surface, color, center, radius) -> Rect
pygame.draw.circle(display, (255, 0, 0), (200, 150), 40)

# line(surface, color, start_pos, end_pos, width=1) -> Rect
pygame.draw.line(display, (0, 0, 255), (80, 120), (300, 160), 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Drawing text

# Text in pygame is drawn in two steps: (1) first we create an image containing the desired text, and then (2) this image is drawn on the screen. 
# It works like this:
import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# Font(pathlib.Path, size) -> Font
game_font = pygame.font.SysFont("Arial", 24)
# render(text, antialias, color, background=None) -> Surface
text = game_font.render("Moikka!", True, (255, 0, 0))
# blit(source, dest, area=None, special_flags=0) -> Rect
display.blit(text, (100, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Here the method `pygame.font.SysFont` creates a font object, which uses the system font Arial in size 24. 
# The the method `render` creates an image of the specified text in the given colour. 
# This image is drawn on the window with the `blit` method, just as before.

# NB: different systems will have different fonts available. 
# If the system this program is exeuted on doesn't have the Arial font, even though Arial is a very common font available on most systems, the default system font is used instead. 
# If you need to have a specific font available for your game, you can include the font file in the game directory and specify its location for the `pygame.font.Font` method.

# Clock - Approach 1

# Please write a program which displays a clock face which displays the system time.

import pygame
from datetime import datetime
from math import pi, sin, cos

width, height = 640, 480
display = pygame.display.set_mode((width, height))

mid_x = width/2
mid_y = height/2

# Computes the total division of the full 2π radian rotation for the hour hand into 43200 seconds - 2π/43,200
radians_per_hoursec = (2 * pi) / (12 * 60 * 60)
# Computes the total division of the full 2π radian rotation for the minute hand into 3600 seconds - 2π/3,600
radians_per_minsec = (2 * pi) / (60 * 60)
# Computes the total division of the full 2π radian rotation for the second hand into 60 seconds - 2π/60
raidans_per_sec = (2 * pi)/ 60

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    now = datetime.now()
    hour = int(f"{now: %H}")
    min = int(f"{now: %M}")
    sec = int(f"{now: %S}")
    # Because the y-axis is reversed from typical (increases top to bottom) and 0 radian starts from the 3 o'clock position, the radians need to move back (anti-clockwise) entirely by π/2 or 90 degrees.
    # https://stackoverflow.com/questions/10473930/how-do-i-find-the-angle-between-2-points-in-pygame rads -= math.pi/2
    # Images\radian-measure-circle.png
    hour_rad = (((hour * 60 * 60) + (min * 60) + sec) * radians_per_hoursec) - pi/2
    min_rad = (((min * 60) + sec) * radians_per_minsec) - pi/2
    sec_rad = (sec * raidans_per_sec) - pi/2
    

    pygame.display.set_caption(f"{now:%H:%M:%S}")
    
    display.fill((0, 0, 0))
    
    # Center Point
    pygame.draw.circle(display, (255, 0, 0), (mid_x, mid_y), 10)
    # Clock Circle
    pygame.draw.circle(display, (255, 0, 0), (mid_x, mid_y), 200, width=5)
    
    # Hour Hand
    pygame.draw.line(display, (0, 0, 255), (mid_x, mid_y), (mid_x+cos(hour_rad)*140, mid_y+sin(hour_rad)*140), width=4)
    
    # Minute Hand
    pygame.draw.line(display, (0, 0, 255), (mid_x, mid_y), (mid_x+cos(min_rad)*180, mid_y+sin(min_rad)*180), width=2)
    
    # Second Hand
    pygame.draw.line(display, (0, 0, 255), (mid_x, mid_y), (mid_x+cos(sec_rad)*180, mid_y+sin(sec_rad)*180), width=1)
    
    pygame.display.flip()
 
    clock.tick(60)     
    
# Clock - Approach 2
import pygame
import math
from datetime import datetime
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
def circle(color: int, radius: int):
    pygame.draw.circle(screen, color, (middle_x, middle_y), radius)
 
def hand(length: int, thickness: int, proportion: float):
    angle = 2*math.pi*proportion-math.pi/2
    end_x = middle_x+math.cos(angle)*length
    end_y = middle_y+math.sin(angle)*length
 
    pygame.draw.line(screen, (0, 0, 255), (middle_x, middle_y), (end_x, end_y), thickness)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    hours = datetime.now().hour%12
    minutes = datetime.now().minute
    seconds = datetime.now().second
 
    pygame.display.set_caption(str(datetime.now().time())[:8])
 
    screen.fill((0, 0, 0))
 
    middle_x = width/2
    middle_y = height/2
 
    circle((255, 0, 0), 200)
    circle((0, 0, 0), 195)
    circle((255, 0, 0), 10)
 
    hand(185, 1, seconds/60)
    hand(180, 2, (minutes+seconds/60)/60)
    hand(150, 5, (hours+minutes/60+seconds/3600)/12)
 
    pygame.display.flip()  

# Asteroids - Approach 1

# Please create a game where asteroids fall from the sky. 
# The player moves a robot left and right and tries to collect the falling rocks. 
# The player gets a point for each asteroid collected, and the points total is shown at the top of the window. 
# The game ends when the player misses an asteroid.

import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Asteroids")

# Robot object, starting position and controls
robot = pygame.image.load("Images\\Pygame\\robot.png")
x = 0
y = height - robot.get_height()

controls = [(pygame.K_LEFT, -2), (pygame.K_RIGHT, 2)]

# Robot Range 
def robot_range(min_x: int):
    # creates a set of coordinate range covering all permutations from a min and max x & y coordinate
    return set(((x, y) for x in range(min_x, min_x + robot.get_width()+1) 
                for y in range(height - robot.get_height(), height+1)))

# Rock & Rock Range
rock = pygame.image.load("Images\\Pygame\\rock.png")
number = 5
rocks = [[-1000, height] for i in range(number)]

def rock_range(rock_pos: list):
    # creates a set of coordinate range covering all permutations from a min and max x & y coordinate
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
        # condition statement checks whether any of the coordinate space of the rock intersects with the robot coordinate space
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
    
# Asteroids - Approach 2
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
pygame.display.set_caption("Asteroids")
 
robot = pygame.image.load("Images\\Pygame\\robot.png")
x = 0
y = height-robot.get_height()
 
rock = pygame.image.load("Images\\Pygame\\rock.png")
number = 5
positions = []
for i in range(number):
    positions.append([randint(0,width-rock.get_width()),-randint(100,1000)])
 
to_right = False
to_left = False
 
points = 0
 
clock = pygame.time.Clock()
 
font = pygame.font.SysFont("Arial", 24)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
 
        if event.type == pygame.QUIT:
            exit()
 
    if to_right:
        x += 2
    if to_left:
        x -= 2
 
    for i in range(number):
        positions[i][1] += 1
        if positions[i][1]+rock.get_height() >= height:
            # game ends
            exit()
        # if the current y-position + height of the rock is same to or greater than the fixed y-position of the robot:
        if positions[i][1]+rock.get_height() >= y:
            robot_middle = x+robot.get_width()/2
            rock_middle = positions[i][0]+rock.get_width()/2
            # if the subtracted mid-widths of the rock and and robot are less than their combined widths divided by 2, there is an overlap 
            if abs(robot_middle-rock_middle) <= (robot.get_width()+rock.get_width())/2:
                # the robot caught an asteroid
                positions[i][0] = randint(0,width-rock.get_width())
                positions[i][1] = -randint(100,1000)
                points += 1
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    for i in range(number):
        screen.blit(rock, (positions[i][0], positions[i][1]))
 
    text = font.render("Points: "+str(points), True, (255, 0, 0))
    screen.blit(text, (width-150, 10))
 
    pygame.display.flip()
 
    clock.tick(60)