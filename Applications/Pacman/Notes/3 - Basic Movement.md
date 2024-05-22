# Basic Movement

## Basics

Now that we have a blank screen let's do something with it. What we will do in this section is draw a yellow circle to the screen, and move it around the screen with the keyboard. We will use the directional keys in order to move Pacman around. Pacman can only move around in one of four directions: up, down, left, and right. Pacman can only move in one of these directions at any one time, he does not move in a diagonal at any time. The basic idea behind movement is that when the player presses a directional key, **LEFT** for example, the yellow circle will move a few pixels to the left. We do that by decreasing it's x value by a certain number of pixels. The more pixels we move the circle the faster it will appear to move. The yellow circle will be our current representation of Pacman, so we'll create a **Pacman** class. Before we can move things around the screen, lets learn a few basic physics.

Why do we need to know physics in order to move something around on the screen? Why can't we just update the x and y positions like we mentioned above? One problem with that, out of many, is that the speed the circle moves will be dependent on the computer the player is using. On a faster computer, the circle will move faster because it will be able to move that many pixels more often than on a slower computer. We want our yellow circle to move at the same speed no matter how fast or slow the computer is. So, in order to do that we need to actually calculate the number of pixels to move rather than have a fixed number of pixels. The number of pixels will be different from computer to computer. But how do we calculate this? That's where some physics come in.

Don't worry, you don't need a degree in Physics to understand this stuff. I do, but that's unrelated. The only thing we'll need to understand is the basic equation for one-dimensional motion. Here it is:

$$s(\Delta t) = s_{0} + v\Delta t + ½ \times a\Delta t^{2}$$

![circle_blackscreen](https://img1.wsimg.com/isteam/ip/51f9eb68-183a-416f-aedc-5c476e4e4d1c/circle.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true)

So in this equation, $s_{0}$ is our current position whether it's our x-position or our y-position. $V$ is our velocity which is a vector so it includes our speed and direction. $s(Δt)$ is our new position. $Δt$ is the time it will take to get us to our new position, and $a$ is the acceleration of our object as it is traveling to the new position. We can simplify this equation quite a bit because our acceleration will always be $0$. You only need acceleration if an object is speeding up or slowing down. Pacman and all of the other things that move in our game are either not moving, or moving at full speed. An object that has constant velocity has 0 acceleration even if it is moving really fast. **Remember that acceleration is just a change in velocity**. So using that fact we can simplify the equation to the following:

$$s(\Delta t) = s_{0} + v\Delta t$$

So, in order to calculate the new position all we need to know is our current position, the direction and speed we want to move in, and the time it will take to get there. In the next section we'll figure out how to deal with this timing issue. It's actually really easy since pygame includes some timing packages.

## Time

We need to initialize a clock. We can define a clock in pygame with the statement below. We need to add this line to the **\_\_init\_\_** method in the **GameController** class in the run.py file.  The **...** just means that there's other code there, but I didn't feel like writing everything out again.  Just add the blue line to the end of the method.

```python
# run.py
def __init__(self):
    ...
    self.clock = pygame.time.Clock()
```

In the update method in our **GameController** class in the run.py file we will add the following line as the first line in that method. What this does is returns the amount of time that has passed since the last time this line was called. We divide that value by 1000 because we want that value to be in units of seconds instead of milliseconds. So on faster computers this line will be called more often, so the value of `dt` will be lower. On slower computers this line won't be called as often so the `dt` value will be higher. `dt` here represents our $Δt$ in the equations above.

```python
# run.py
def update(self):
    dt = self.clock.tick(30) / 1000.0
    self.checkEvents()
    self.render()
```

## Add Constants

Pacman is yellow, so lets add a new color here:  Yellow.  Yellow is a mixture of red and green so we set those to 255 and blue to 0.

We'll also define the four directions along with a STOP variable.  The values here don't actually matter, just as long as they are all different.  So I'm at least making opposite directions opposite in value.  You'll see why that's desirable later on.  The reason I am doing it this way is because I want to create a dictionary later on and use these as the keys to that dictionary.  A dictionary requires a <key:value> pair and each key has to be unique.  So these are basically the keys to the dictionary I'm about to create.  

```python
# constants.py
...
YELLOW = (255, 255, 0)

STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

PACMAN = 0
```

## Pacman

Well, we have everything in place, so now we can actually create our Pacman object. We can just simply draw a circle and move it around, but let's put in some extra work and actually make a Pacman class that we'll build off of in later sections.

We'll create a file called **pacman.py** and as we've done before we'll start the file off with some imports. These lines should look familiar to you by now I hope.

This is the start of the Pacman class. When we create a Pacman object we'll give it a name of "pacman". We don't have to do this, but it'll come in handy later on. We also give it an initial position of (200, 400). This will change later on, but for now you can input any initial position here.

This is also where I create the directions dictionary with the keys from above. The values are just the corresponding Vectors.  The initial direction of Pacman is STOP because we don't want him moving unless we say so. We also specify his speed, color, and radius. The radius is just how big we want him to be since at this time we're just going to represent Pacman as a yellow circle with a radius of 10 pixels.

In the update method we check to see if any of the valid keyboard keys are being pressed. We then use that direction to move the yellow circle.

Notice for Pacman's speed we have `100 * TILEWIDTH/16`.  This is so that Pacman's speed is always the same relative to the size of the maze since by default each tile in our maze is 16x16 pixels. If you instead change the maze to other sizes like 8x8, 24x24, 32x32 or 64x64 then Pacman won't appear to move too fast or too slow.

```python
# pacman.py
import pygame
from pygame.locals import *
from vector import Vector2
from constants import *

class Pacman(object):
    def __init__(self):
        self.name = PACMAN
        self.position = Vector2(200, 400)
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.direction = STOP
        self.speed = 100 * TILEWIDTH/16
        self.radius = 10
        self.color = YELLOW

    def update(self, dt):
        self.position += self.directions[self.direction]*self.speed*dt
        direction = self.getValidKey()
        self.direction = direction
```

We also check for key presses since we want to detect if the user is pressing the correct keys. If we detect that the user has pressed either the UP, DOWN, LEFT, or RIGHT keys then we can just return the corresponding key. If none of these keys are being pressed, then we return the STOP key.

```python
# pacman.py
def getValidKey(self):
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_UP]:
        return UP
    if key_pressed[K_DOWN]:
        return DOWN
    if key_pressed[K_LEFT]:
        return LEFT
    if key_pressed[K_RIGHT]:
        return RIGHT
    return STOP
```

We need to be able to draw Pacman to the screen so we include his own render method here. Like I said before we're representing him as a circle, so that's what we'll draw to the screen. In pygame when we draw circles, the position of the circle has to be integers instead of floats. So when drawing the circle here we are going to call the vectors **asInt** method. If we leave them as floats, then pygame will throw a fit. It only does this for circles for some reason.

```python
# pacman.py
def render(self, screen):
    p = self.position.asInt()
    pygame.draw.circle(screen, self.color, p, self.radius)
```

Now that we have our Pacman class we can go back to the **run.py** file and make a Pacman object from our class. Follow the simple steps below and we'll be good to go.

At the top of the run.py file we need to import our pacman.py file so we can use the Pacman class.  

Remove the word 'pass' from the **startGame()** method and create the Pacman object.

In the **update()** method, right after we get the value for dt, we'll make a call to pacman's update method passing in the dt value we got from the previous line.

Finally, we modify our **render()** method by adding these two lines. We want these two lines to appear before the line we've already added which updates the display. The first one we add in order to redraw the background. If we don't add this and if there are any objects that move, they'll appear as if they are smearing across the screen. We need to erase the objects and redraw them at their new positions. The object will still move, but all of the images of the object at the previous positions will still be on screen as well. So we need to basically erase all of the objects and redraw them at their new positions.  Try the code out with this line commented out to see what I mean. And of course we need to tell the Pacman object to render as well.

```python
# run.py
...
from pacman import Pacman 

def startGame(self):
    ...
    self.pacman = Pacman()

def update(self):
    dt = self.clock.tick(30) / 1000.0
    self.pacman.update(dt)
    self.checkEvents()
    self.render()

def render(self):
    self.screen.blit(self.background, (0, 0))
    self.pacman.render(self.screen)
    pygame.display.update()
```
