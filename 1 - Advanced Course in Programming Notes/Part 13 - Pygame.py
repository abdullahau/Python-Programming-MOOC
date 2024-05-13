# First Pygame program

# Here is a simple program for checking your pygame installation works correctly:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

window.fill((0,0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
# The program only consists of displaying a window, and it runs until the user closes the window.

# Let's take a closer look at the steps required to achieve this. 
# The first line takes the pygame library into use: `import pygame`. 
# The next command `pygame.init` initializes the pygame modules, 
# and the next one creates a window with the function `pygame.display.set_mode`.

pygame.init()
window = pygame.display.set_mode((640, 480))

# The `set_mode` function takes the window dimensions as an argument. 
# The tuple `(640, 480)` indicates that the window is 640 pixels wide and 480 pixels high. 
# The variable name `window` can be used later to access the window, for example to draw something in it.

# The following two commands do just that:

window.fill((0, 0, 0))
pygame.display.flip()

# The `fill` method fills the window with the colour passed as an argument. 
# In this case the colour is black, passed as an RGB value in the tuple `(0, 0, 0)`. 
# The `pygame.display.flip` updates the contents of the window.

# After these initialization commands the _main loop_ of the program begins:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# The main loop handles all events the operating system passes to the program. 
# With each iteration the function `pygame.event.get` returns a list of any events collected since the previous iteration.

# In the example above the program only handles events of type `pygame.QUIT`. 
# This event is raised by, for example, clicking on the exit button in the corner of the window. 
# If the `pygame.QUIT` event is raised, the program exits through the `exit` function.

# You can try and see what happens if your program doesn't handle the `pygame.QUIT` event. 
# This should mean that clicking on the exit button does nothing, which would be confusing for the user. 
# As the program is run from the command line, you can still stop it from the command line with Control+C.

# Add an image

# Let's add an image to the window:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('Images\\Pygame\\robot.png')

window.fill((0, 0, 0))
window.blit(robot, (100, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# The program uses this image of a robot, which is stored in the file `robot.png`:

# The function `pygame.image.load` loads the image in the file `robot.png` and stores a reference to it in the variable named `robot`. 
# The method `blit` draws the image at the location `(100, 50)`, and the function `pygame.display.flip` updates the window contents, as before. 
# The location `(100, 50)` means that the _top left corner_ of the image is at that location within the window.

# In pygame the origo point `(0, 0)` is in the top left corner of the window. 
# The x coordinates increase to the right, and the y coordinates increase downwards, so that the bottom right corner has the coordinates `(640, 480)`. 
# This is contrary to how coordinates are usually handled in e.g. mathematics, but it is quite common in a programming context, and worth getting used to.

# Once you have loaded an image, you can use it many times within the same window. 
# The following code draws the image of the robot at three different locations:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('Images\\Pygame\\robot.png')

window.fill((0, 0, 0))
window.blit(robot, (0, 0))
window.blit(robot, (300, 0))
window.blit(robot, (100, 200))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Here we set the location of the image so that it lies at the centre of the window:

width = robot.get_width()
height = robot.get_height()
window.blit(robot, (320-width/2, 240-height/2))

# Implementation

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('Images\\Pygame\\robot.png')

window.fill((0, 0, 0))
half_x = 640/2
half_y = 480/2
width = robot.get_width()
height = robot.get_height()
window.blit(robot, (half_x-width/2, half_y-height/2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# The method `get_width` returns the width of the image, and the method `get_height` returns its height, both in pixels. 
# The centre of the window is at half its width and height, so at `(320, 240)`, which we can use to calculate a suitable location for the top left corner of the image, so that it lies exactly at the centre.

# Four robots - Approach 1

# Please write a program which draws a robot in each of the four corners of the window.

import pygame

pygame.init()
window_x = 640
window_y = 480
window = pygame.display.set_mode((window_x, window_y))

robot = pygame.image.load('Images\\Pygame\\robot.png')

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()

window.blit(robot, (0, 0))
window.blit(robot, (window_x - width, 0))
window.blit(robot, (0, window_y - height))
window.blit(robot, (window_x - width, window_y - height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


# Four robots - Approach 2

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
right_x = width-robot.get_width()
down_y = height-robot.get_height()
 
screen.fill((0, 0, 0))
screen.blit(robot, (0, 0))
screen.blit(robot, (right_x, 0))
screen.blit(robot, (0, down_y))
screen.blit(robot, (right_x, down_y))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Robots in a row - Approach 1

# Please write a program which draws ten robots in a row. 

import pygame

pygame.init()
window_x, window_y = 640, 480
window = pygame.display.set_mode((window_x, window_y))

robot = pygame.image.load('Images\\Pygame\\robot.png')

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

# Robots in a row - Approach 2
import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
for i in range(10):
    screen.blit(robot, (50+50*i, 100))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# A hundred robots - Approach 1

# Please write a program which draws a hundred robots: ten rows with ten robots in each row.

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('Images\\Pygame\\robot.png')

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

# A hundred robot - Approach 2
import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
for i in range(10):
    for j in range(10):
        screen.blit(robot, (20+10*i+40*j, 100+i*20))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Random robots - Approach 1

# Please write a program which draws _a thousand_ robots in random places.

import pygame
from random import randint
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("Images\\Pygame\\robot.png")
 
screen.fill((0, 0, 0))

right_x_limit = 640 - robot.get_width()
down_y_limit = 480 - robot.get_height()

for i in range(1000):
    screen.blit(robot, (randint(0 , right_x_limit), randint(0, down_y_limit)))
        
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Random robots - Approach 2

import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
for i in range(1000):
    x = randint(0,width-robot.get_width())
    y = randint(0,height-robot.get_height())
    screen.blit(robot, (x,y))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()