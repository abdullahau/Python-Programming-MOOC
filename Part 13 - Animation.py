# Animation

# Many games have moving characters, so a logical next step is creating animations. 
# We can create the illusion of movement by drawing the same image in different locations on the screen and timing the changes appropriately.

# Creating an animation

# The following code creates an animation where a robot moves from left to right in a pygame window:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += 1
    clock.tick(60)

# Let's take a closer look at the commands involved. 
# If we want to trace the movement of the image on the screen, we need to know its location, 
# which is why we have two variables for the coordinates of the top left corner of the image:

x = 0
y = 0

# We also have a clock, which we use to make sure the speed of the animation is just right:

clock = pygame.time.Clock()

# The main loop draws the image at its current location with each iteration:

window.fill((0, 0, 0))
window.blit(robot, (x, y))
pygame.display.flip()

# First the method `fill` fills the window with black, as before. 
# The colour is passed as a tuple containing the RGB values for the colour. 
# In this case the argument is `(0, 0, 0)`, which means that all three components - red, green and blue - have value 0. 
# Each component can have a value between 0 and 255. 
# So, if we passed `(255, 255, 255)` as the argument, we'd get a white window, and with `(255, 0, 0)` we'd get a red window. 
# RGB colour codes form the backbone of digital colouring, and there are many tools online for working with them, for example [RGB Color Codes Chart](https://www.rapidtables.com/web/color/RGB_Color.html).

# After the window is filled with colour the image is drawn at the given location with the `blit` method. 
# Then the contents of the window are updated with the function `pygame.display.flip`.

# Finally, the value stored in `x` is incremented, which makes the image move one pixel to the right with each iteration:

# The clock method `tick` is called at the end:
clock.tick(60)

# The method `tick` takes care of the speed of the animation. 
# The argument `60` dictates that the loop should be executed 60 times a second, which means that the image moves 60 pixels to the right each second. 
# This approximately matches the _FPS_ or _frames per second_ value used with games.

# In principle, the `tick` method makes sure that the animation runs at the same speed on every computer. 
# If there was no such timing involved, the speed of the animation would depend on the speed of the computer.

# Bouncing off a wall

# The previous animation was otherwise excellent, but as the robot reached a wall, it just kept going out of sight. 
# Let's make the robot bounce off the wall.
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(60)

# There is a new variable `velocity` which determines the direction of the movement. 
# If the value is above zero, movement is to the right, and if it is below zero, movement is to the left. 
# More precisely in this case, if the value is `1`, the robot moves to the right, and if it is `-1`, the robot moves to the left.

# The following lines make the robot bounce off the side walls:
if velocity > 0 and x+robot.get_width() >= 640:
    velocity = -velocity
if velocity < 0 and x <= 0:
    velocity = -velocity

# If the velocity is above zero so that the robot is moving to the right, and the right edge of the image goes beyond the right edge of the window, the direction is reversed and the robot starts moving to the left. 
# Similarly, if the velocity is below zero so that the robot is moving to the left, and the left edge of the image reaches the left edge of the window, the direction is again reversed and the robot starts moving to the right again.

# This makes the robot move on a path from the left edge of the window to the right edge, and back to the left, and then to the right again, repeated ad infinitum.

# Rotation

# Let's create one more animation. 
# This time the robot should _rotate_ in a circle around the centre of the window:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320+math.cos(angle)*100-robot.get_width()/2
    y = 240+math.sin(angle)*100-robot.get_height()/2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
    
# Rotation in a relatively precise circle is achieved with the help of some basic trigonometric functions. 
# The varible `angle` contains the angle of the robots location in relation to the centre of the window and the horizontal line running through it. 
# The sine and cosine functions from the Python math library are used to calculate the coordinates of the robot's location:
x = 320+math.cos(angle)*100-robot.get_width()/2
y = 240+math.sin(angle)*100-robot.get_height()/2

# We are utilizing circular functions to determine the x and y coordinate such that $x = cos(t)\times r$ and $y = sin(t) \times r$, where $r = radius$, $t = angle \space in \space radians$ and $(x,y)$ are the coordinates of the intersection of the terminal side and the circle of radius *r*

# To ensure that the object rotates around in circle anchored by the middle of the object itself and around the center of the window (320, 240), 
# we need to add the x-origin coordinate and reduce the computed x-coordinate by half the width of the object 
# and add the y-origin coordinate and reduce the y-coordinate by half the height of the object 
# such that the formula now looks like: $x = (x {-} origin + cos (t) \times r) - w/2$ and $y = (y {-} origin + sin (t) \times r) - h/2$ where $w = width$ and $h = height$. 

# The robot rotates around a circle of radius 100 around the centre of the window. 
# The hypotenuse in this scenario is the radius of the circle.
# The cosine function gives the length of the _adjacent_ side of a right triangle in relation to the hypotenuse, which means that it gives us the `x` coordinate of the location. 
# The sine function gives the length of the _opposite_ side, i.e. the `y` coordinate. 
# The location is then adjusted so that the centre of the circle is at the centre of the window and the location is also adjusted for the size of the image, so the image is anchored about its center.

# With each iteration the size of the `angle` is incremented by 0.01 *rad*. 
# As we are using radians, a full circle is 2π, which equals about 6.28 *rad*. It takes about 628 ($6.28 / 0.01=628$) iterations for the robot to go a full circle, and at 60 iterations per second this takes just over 10 seconds.

# The modified code below shows the circle around which the robot image is rotating, a line tracking the movement of the robot's center and upper left edge, and the length of both the lines.
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Images\\Pygame\\robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320+math.cos(angle)*100-robot.get_width()/2
    y = 240+math.sin(angle)*100-robot.get_height()/2
    
    window.fill((0, 0, 0))
    
    
    # Reference lines - Tracks the top left edge of the robot images
    pygame.draw.line(window, (0, 0, 225), (320, 240), (x, y))
    blue_line_length = ((math.cos(angle)*100-robot.get_width()/2)**2 + (math.sin(angle)*100-robot.get_height()/2)**2)**(1/2)
    
    # Reference line - Tracks the center of the robot image or the coordinates as per the current angle
    pygame.draw.line(window, (255, 0, 0), (320, 240), (320+math.cos(angle)*100, 240+math.sin(angle)*100))
    red_line_length = ((math.cos(angle)*100)**2 + (math.sin(angle)*100)**2)**(1/2)
    
    # Reference circle - a reference circle at the center of the window (320, 240) with a radius of 100
    pygame.draw.circle(window, (255, 255, 255), (320, 240), 100, width=1)
    

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 20)
    # create a text surface object,
    # on which text is drawn on it.
    angle_text = font.render(f"{angle = : .2f}", True, (0, 255, 0))
    blue_line_text = font.render(f"{blue_line_length = : .2f}", True,(0, 255, 0))
    red_line_text = font.render(f"{red_line_length = : .2f}", True,(0, 255, 0))
    # create a rectangular object for the
    # text surface object
    angleRect = angle_text.get_rect()
    blueRect = blue_line_text.get_rect()
    redRect = red_line_text.get_rect()
    # set the center of the rectangular object.
    angleRect.center = (400, 400)
    blueRect.center = (400, 420)
    redRect.center = (400, 440)
    window.blit(angle_text, angleRect)
    window.blit(blue_line_text, blueRect)
    window.blit(red_line_text, redRect)
    
    window.blit(robot, (x, y))
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
    
# Vertical movement - Approach 1

# Please create an animation where the robot moves up and down in an endless loop.

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Images\\Pygame\\robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += velocity
    if velocity > 0 and y + robot.get_height() >= 480:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)

# Vertical movement - Approach 2

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x = 0
y = 0
speed = 1
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
 
    y += speed
    if speed > 0 and y+robot.get_height() >= height:
        speed = -speed
    if speed < 0 and y <= 0:
        speed = -speed
 
    clock.tick(60)
    
# Round the perimeter - Approach 1

# Please create an animation where the robot traces the perimeter of the window.

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("Images\\Pygame\\robot.png")

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
    
# Round the perimeter - Approach 2
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x = 0
y = 0
direction = 1 # 1 = to right, 2 = to down, 3 = to left, 4 = to up
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
 
    if direction == 1:
        x += 1
        if x+robot.get_width() == width:
            direction = 2
    elif direction == 2:
        y += 1
        if y+robot.get_height() == height:
            direction = 3
    elif direction == 3:
        x -= 1
        if x == 0:
            direction = 4
    elif direction == 4:
        y -= 1
        if y == 0:
            direction = 1
 
    clock.tick(60)

# Two robots - Approach 1

# Please create an animation where two robots move back and forth to the left and right. 
# The lower robot should move at double the speed of the upper one.

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("Images\\Pygame\\robot.png")

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
    
    bottom_x += bottom_velocity
    
    if top_velocity > 0 and top_x+robot.get_width() >= 640:
        top_velocity = -top_velocity
    if top_velocity < 0 and top_x <= 0:
        top_velocity = -top_velocity

    if bottom_velocity > 0 and bottom_x+robot.get_width() >= 640:
        bottom_velocity = -bottom_velocity
    if bottom_velocity < 0 and bottom_x <= 0:
        bottom_velocity = -bottom_velocity        
    

    clock.tick(60)
    
# Two robots - Approach 2
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x1 = 0
x2 = 0
speed1 = 1
speed2 = 2
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    x1 += speed1
    if x1 == 0 or x1+robot.get_width() == width:
        speed1 = -speed1
    x2 += speed2
    if x2 == 0 or x2+robot.get_width() == width:
        speed2 = -speed2
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, 50))
    screen.blit(robot, (x2, 200))
    pygame.display.flip()
 
    clock.tick(60)

# Robots in a circle - Approach 1

# Please create an animation where ten robots go round in a circle. 

import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Images\\Pygame\\robot.png")

radius = 130
center_x = 640/2
center_y = 480/2
angle = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    pygame.draw.circle(window, (0, 255, 0), (center_x, center_y), radius, width=1)
    pygame.draw.line(window, (255, 0, 0), (center_x, center_y), (center_x+math.cos(angle)*radius, center_y+math.sin(angle)*radius))
    
    for i in range(10):
        rad = angle + (i * (2 * math.pi)/10)
        x = center_x + math.cos(rad) * radius - robot.get_width()/2
        y = center_y + math.sin(rad) * radius - robot.get_height()/2
        window.blit(robot, (x, y))
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)


# Robots in a circle - Approach 1 Submitted
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("Images\\Pygame\\robot.png")

radius = 130
center_x = 640/2
center_y = 480/2
angle = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    for i in range(10):
        rad = angle + (i * (2 * math.pi)/10)
        x = center_x + math.cos(rad) * radius - robot.get_width()/2
        y = center_y + math.sin(rad) * radius - robot.get_height()/2
        window.blit(robot, (x, y))
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
    
# Robots in a circle - Approach 2
import pygame
import math
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
angle = 0
radius = 150
number = 10
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.fill((0, 0, 0))
    for i in range(number):
        x = width/2+math.cos(angle+2*math.pi*i/number)*radius-robot.get_width()/2
        y = height/2+math.sin(angle+2*math.pi*i/number)*radius-robot.get_height()/2
        screen.blit(robot, (x, y))
    pygame.display.flip()
 
    angle += 0.01
    clock.tick(60)

# Bouncing ball - Approach 1

# Please create an animation where a ball bounces from the edges of the window.

'''
Pusedocode:

1. Initialize variables:
   - Ball position (x, y)
   - Ball velocity (vx, vy)
   - Screen width (width)
   - Screen height (height)
   - Ball radius (radius)
2. Loop:
   a. Update ball position:
      - x = x + vx
      - y = y + vy
   b. Check for collision with walls:
      - If (x - radius < 0) or (x + radius > width), reverse the x velocity (vx = -vx).
      - If (y - radius < 0) or (y + radius > height), reverse the y velocity (vy = -vy).
   c. Render/update ball position on the screen.
   d. Pause for a short time to control the frame rate.
3. End loop
'''

import pygame
from random import randint

pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("Images\\Pygame\\ball.png")

clock = pygame.time.Clock()

x = randint(5, width - ball.get_width())
y = randint(5, height - ball.get_height())
x_direction = 1
y_direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    if x == 0 or x == width - ball.get_width():
        x_direction = -x_direction
    
    if y == 0 or y == height - ball.get_height():
        y_direction = -y_direction
    
    x += x_direction
    y += y_direction
    
    window.blit(ball, (x, y))
    
    pygame.display.flip()

    clock.tick(80)
    
# Bouncing ball - Approach 2
import pygame
import math
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
ball = pygame.image.load("ball.png")
 
x = 0
y = 0
ball_x = 2
ball_y = 2
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    x += ball_x
    y += ball_y
 
    if x == 0 or x+ball.get_width() == width:
        ball_x = -ball_x
    if y == 0 or y+ball.get_height() == height:
        ball_y = -ball_y
 
    screen.fill((0, 0, 0))
    screen.blit(ball, (x, y))
    pygame.display.flip()
 
    clock.tick(60)
    
# Robot invasion - Approach 1

# Please create an animation where robots fall from the sky randomly. 
# When a robot reaches the ground, it starts moving to the left or to the right, and finaly disappears off the screen.

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
    
# ⭐⭐ Robot invasion - Approach 2
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("Images\\Pygame\\robot.png")
 
# number of robots (the same robots are reused)
number = 20
 
robots = []
for i in range(number):
    # causes the new random start position to be drawn immediately
    robots.append([-1000,height])
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    for i in range(number):
        if robots[i][1]+robot.get_height() < height:
            # the robot falls downwards
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > width:
                # new random start point
                robots[i][0] = randint(0,width-robot.get_width())
                robots[i][1] = -randint(100,1000)
            elif robots[i][0]+robot.get_width()/2 < width/2:
                # the robot moves to the left
                robots[i][0] -= 1
            else:
                # the robot moves to the right
                robots[i][0] += 1
 
    screen.fill((0, 0, 0))
    
    for i in range(number):
        screen.blit(robot, (robots[i][0], robots[i][1]))

    pygame.display.flip()
 
    clock.tick(60)