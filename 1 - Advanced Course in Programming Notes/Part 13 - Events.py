# Events

# Thus far our main loops have only executed predetermined animations and reacted to only `pygame.QUIT` type events.

# Handling events

# This program prints out information about all the events passed by the operating system to the pygame program, while it is running:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()

# Let's assume the program was left running for a while, and then the exit button was clicked. 
# The program prints out the following info:

'''
<Event(4-MouseMotion {'pos': (495, 274), 'rel': (495, 274), 'buttons': (0, 0, 0), 'window': None})>
<Event(4-MouseMotion {'pos': (494, 274), 'rel': (-1, 0), 'buttons': (0, 0, 0), 'window': None})>
<Event(4-MouseMotion {'pos': (492, 274), 'rel': (-2, 0), 'buttons': (0, 0, 0), 'window': None})>
<Event(4-MouseMotion {'pos': (491, 274), 'rel': (-1, 0), 'buttons': (0, 0, 0), 'window': None})>
<Event(5-MouseButtonDown {'pos': (491, 274), 'button': 1, 'window': None})>
<Event(6-MouseButtonUp {'pos': (491, 274), 'button': 1, 'window': None})>
<Event(2-KeyDown {'unicode': 'a', 'key': 97, 'mod': 0, 'scancode': 38, 'window': None})>
<Event(3-KeyUp {'key': 97, 'mod': 0, 'scancode': 38, 'window': None})>
<Event(2-KeyDown {'unicode': 'b', 'key': 98, 'mod': 0, 'scancode': 56, 'window': None})>
<Event(3-KeyUp {'key': 98, 'mod': 0, 'scancode': 56, 'window': None})>
<Event(2-KeyDown {'unicode': 'c', 'key': 99, 'mod': 0, 'scancode': 54, 'window': None})>
<Event(3-KeyUp {'key': 99, 'mod': 0, 'scancode': 54, 'window': None})>
<Event(12-Quit {})>
'''

# The first few events concern mouse usage, ten there are some events from the keyboard, and finally the last event closes the program. 
# Each event has at least a type, but they may also offer some other identifying info, such as the location of the mouse cursor or the key that was pressed.

# You can look for event descriptions in the [pygame documentation](https://www.pygame.org/docs/ref/event.html), 
# but it can sometimes be easier to print out events with the code above, and look for the event that occurs when something you want to react to happens.

# Keyboard events

# This program can process events where the user presses the arrow key either to the right or to the left on their keyboard. 
# The program prints out which key was pressed.

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")

        if event.type == pygame.QUIT:
            exit()

# The constants `pygame.K_LEFT` and `pygame.K_RIGHT` refer to the arrow keys to the left and right. 
# The pgyame key constants for the different keys on a keyboard are listed in the [pygame documentation](https://www.pygame.org/docs/ref/key.html#key-constants-label).

# For example, if the user presses the arrow key to the right twice, then the left one once, and then the right one once more, the program prints out
'''
right
right
left
right
'''

# We now have all the tools needed to move a character, or _sprite_, on the screen to the right and left with the arrow keys. 
# The following code will achieve this:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
# In the code above we have the variables `x` and `y` which contain the coordinate location for the sprite. 
# The variable `y` is set so that the sprite appears at the bottom of the window. 
# The `y` value does not change throughout the execution of the program. 
# The `x` value, however, increases by 10 whenever the user presses the arrow key to the right, and decreases by 10 whenever the left arrow key is pressed.

# The program works otherwise quite well, but the key needs to be pressed again each time we want to move again. 
# It would be better if the movement was continuous as the key was held down. 
# The following program offfers this functionality:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

to_right = False
to_left = False

clock = pygame.time.Clock()

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

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)

# The code now contains the variables `to_right` and `to_left`. 
# These contain knowledge of whether the sprite should be moving to the right or to the left at any given moment. 
# When the user presses down an arrow key, the value stored in the relevant variable become `True`. When the key is released, the value changes to `False`.

# The clock is used to time the movements of the sprite, so that they potentially happen 60 times each second. 
# If an arrow key is pressed, the sprite moves two pixels to the right or to the left. 
# This means the sprite moves 120 pixels per second if the key is kept pressed down.

# Four directions

# Please write a program where the player can move a robot in four directions with the arrow keys on the keyboard.

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Images\\Pygame\\robot.png")
x = (640-robot.get_width())/2
y = (480-robot.get_height())/2

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

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
    
# Four walls - Approach 1

# Please improve the program in the previous exercise so that the robot cannot pass outside the window in any of the four directions.

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("Images\\Pygame\\robot.png")
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
    
# Four walls - Approach 2

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
x = width/2-robot.get_width()/2
y = height/2-robot.get_height()/2
 
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
 
    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2
 
    x = max(x,0)
    x = min(x,width-robot.get_width())
    y = max(y,0)
    y = min(y,height-robot.get_height())
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
 
    clock.tick(60)

# Two players - Approach 1

# Please write a program where two players each direct their own robot. 
# One of the players should use the arrow keys while the other could use, for example, the w-s-a-d keys.

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("Images\\Pygame\\robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

robot1 = pygame.image.load("Images\\Pygame\\robot.png")
x1 = width - robot_width/2
y1 = height - robot_width/2

to_right_r1 = False
to_left_r1 = False
to_up_r1 = False
to_down_r1 = False

robot2 = pygame.image.load("Images\\Pygame\\robot.png")
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


# Two players - Approach 2

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# positions of robots
positions = [[0, 0],
          [width-robot.get_width(), height-robot.get_height()]]
 
controls = []
# key, which robot moves, horizontal movement, vertical movement
controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, 0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, 0, -2))
controls.append((pygame.K_s, 1, 0, 2))
 
clock = pygame.time.Clock()
 
key_pressed = {}
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True
 
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
 
        if event.type == pygame.QUIT:
            exit()
 
    for key in controls:
        if key[0] in key_pressed:
            positions[key[1]][0] += key[2]
            positions[key[1]][1] += key[3]
 
    screen.fill((0, 0, 0))
    for i in range(2):
        screen.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
 
    clock.tick(60)

# 1) positions[0] list stores the starting/current position of the player controlling the up, down, left, right arrows and the index ID reference to his position is also stored in the first index of the tuple in the controls list. Meanwhile, positions[1] holds the starting/current position of the player controlling the W,S,D,A keys.
# 2) controls is a list of tuples containing the information about the key constant, player number (used as index reference to positions), x-axis movement, and y-axis movement.
# 3) With every iteration of the while loop, pygame.event.get() captures all the key events and enters a for loop of all the events captured.
# 4) If the event.type of the event was a KEYDOWN, a dictionary stores the event.key as its key and value of True.
# 5) if the event.type of the event was a KEYUP, dictionary entries of all related event.key are deleted.
# 6) Following the pygame.event.get(), a for loop is used to traverse the controls list and for every entry in the list, an if-statement checks whether the dictionary of all captured keyboard events match the associated controls entry.
# 7) If there is a match, positions[0] and/or positions[1] items in the positions list is updated to the current coordinates of the associated player.
# 8) The last for-loop displays the both the positions with a robot image. 

# Explanation & Unpacking of controls loop:
for key in controls:
    button, player, x, y = key
    if button in key_pressed:
        positions[player][0] += x
        positions[player][1] += y

# Mouse events

# The following code reacts to events where a mouse button is pressed down while the cursor is within the window area:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("you pressed the button number", event.button, "at location", event.pos)

        if event.type == pygame.QUIT:
            exit()

# The execution of this program should look more or less like this:

'''
you pressed the button number 1 at location (82, 135)
you pressed the button number 1 at location (369, 135)
you pressed the button number 1 at location (269, 297)
you pressed the button number 3 at location (515, 324)
'''

# Button number 1 refers to the left mouse button and button number 3 refers to the right mouse button. 

# This next program combines mouse event handling and drawing an image on the screen. 
# When the user presses a mouse button while the mouse cursor is within the bounds of the window, an image of a robot is drawn at that location. 

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]-robot.get_width()/2
            y = event.pos[1]-robot.get_height()/2

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()

# The following program contains an animation where the robot sprite follows the mouse cursor.
# The location of the sprite is stored in the variables `robot_x` and `robot_y`. 
# When the mouse moves, its location is stored in the variables `target_x` and `target_y`. 
# If the robot is not at this location, it moves to the approproate direction.

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    if robot_x > target_x:
        robot_x -= 1
    if robot_x < target_x:
        robot_x += 1
    if robot_y > target_y:
        robot_y -= 1
    if robot_y < target_y:
        robot_y += 1

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
    
# Robot and mouse

# Please write a program where the robot follows the mouse cursor so that the centre of the robot is always directly at the mouse cursor.

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Images\\Pygame\\robot.png")

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            robot_x = event.pos[0]-robot.get_width()/2
            robot_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)

# Robot and mouse - Approach 2
import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0]-robot.get_width()/2
            y = event.pos[1]-robot.get_height()/2
 
            screen.fill((0, 0, 0))
            screen.blit(robot, (x, y))
            pygame.display.flip()
 
        if event.type == pygame.QUIT:
            exit()

# The location of the robot

# Please write a program where the robot appears at a random location within the window. 
# When the player clicks on the robot with the mouse, the robot moves to a new location.

import pygame
from random import randint, choice
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("Images\\Pygame\\robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

robot_pos = (randint(0, width - robot_width), randint(0, height - robot_height))

def robot_range(robot_pos: tuple):
    min_x = robot_pos[0]
    max_x = robot_pos[0] + robot_width
    min_y = robot_pos[1]
    max_y = robot_pos[1] + robot_height
    return [list(range(min_x, max_x)), list(range(min_y, max_y))]

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pip = robot_range(robot_pos)
            if event.pos[0] in pip[0] and event.pos[1] in pip[1]:
                x_cord = choice([i for i in range(0, width - robot_width) if i not in pip[0]])
                y_cord = choice([i for i in range(0, height - robot_height) if i not in pip[1]])
                robot_pos = (x_cord, y_cord)
 
        if event.type == pygame.QUIT:
            exit()
    
    screen.fill((0, 0, 0))
    screen.blit(robot, robot_pos)
    pygame.display.flip()

# The location of the robot - Approach 2
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x = randint(0, width-robot.get_width())
y = randint(0, height-robot.get_height())
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
 
            hit_x = mouse_x >= x and mouse_x <= x+robot.get_width()
            hit_y = mouse_y >= y and mouse_y <= y+robot.get_height()
 
            if hit_x and hit_y:
                x = randint(0, width-robot.get_width())
                y = randint(0, height-robot.get_height())
 
        if event.type == pygame.QUIT:
            exit()
 
        screen.fill((0, 0, 0))
        screen.blit(robot, (x, y))
        pygame.display.flip()