# Node movement (Part 1)

## Basics

So the whole point of creating the node map was to constrain Pacman's movement so that he can only move from node to node and nowhere else. This section will show you how to do that. We will cover three types of node movement, each one building off of the other.

Having a map of connected nodes is great, but now we have to teach Pacman how to move around the maze from node to node. The first type of movement we're going to teach him is simply jumping from node to node. For example, let's say that we have two nodes A and B connected to each other. If Pacman is on Node A and Node A has a neighbor to the LEFT called Node B, then if the player pressed the LEFT key, Pacman would immediately appear on Node B without any indication of movement between the two nodes. If Node A didn't have a neighbor to the LEFT and the player pressed the LEFT key, then nothing would happen. This really isn't how Pacman moves around the maze, but it's a first step and has a lot of useful applications and we'll actually use it for some of the things in the game like menu selection and such. Let's just dive right into the necessary code changes we need to make. Surprisingly, there isn't that much we need to modify.

![pacman_node](https://img1.wsimg.com/isteam/ip/51f9eb68-183a-416f-aedc-5c476e4e4d1c/nodemove1.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true)

## Changes To Pacman

The first thing we're going to modify is the **pacman.py** file. We need to pass in the list of nodes that make up the maze. Instead of specifying a random pixel position vector for Pacman to start out on we need to tell him which node we want him to start out on. Right now it doesn't matter so we'll just have him start out on the first node, so we set his position to be the same as that nodes position. So nodes is the `NodeGroup` class and node is the node that Pacman is currently on. Then we call a method called `setPosition`.

We need to create a new method in the Pacman class. All this method really does is copy the node's position to Pacman's position. We call the copy method because we don't want the same position object associated with Pacman and the node. If it is then modifying Pacman's position will also modify the nodes position. The node will basically follow Pacman around. So instead we copy the position which gives us a fresh new vector to represent Pacman's position.

We need to modify Pacman's **update** method. In the update method we're going to temporarily comment out the position update.  Don't delete it, just comment it out for now. This is only temporary to show you this type of movement though. We also remove the else condition since we don't make Pacman stop based on key presses. From here on out we'll make him stop via conditions in the code.

The other two new methods,  **validDirection** and **getNewTarget**, checks whether the key we're pressing is a valid direction and whether there is a node in that direction. If so, then we move Pacman to that node automatically.

```python
# pacman.py
class Pacman(object):
    def __init__(self, node):
        self.name = PACMAN
        # self.position = Vector2(200, 400)
        self.directions = {UP:Vector2(0, -1), DOWN:Vector2(0, 1), 
                           LEFT:Vector2(-1, 0), RIGHT:Vector2(1, 0), STOP:Vector2()}
  
        self.direction = STOP
        self.speed = 100
        self.radius = 10
        self.color = YELLOW
        self.node = node
        self.setPosition()

    def setPosition(self):
        self.position = self.node.position.copy()

    def update(self, dt):    
        # self.position += self.directions[self.direction]*self.speed*dt 
        direction = self.getValidKey()
        self.direction = direction
        self.node = self.getNewTarget(direction)
        self.setPosition()
        
    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.neighbors[direction] is not None:
                return True
        return False

    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.neighbors[direction]
        return self.node
```

## Changes to GameController

In the **run.py** file we're going to modify the **startGame** method so that we pass in the node we want Pacman to start on. The first node in the list is as good as any for the time being.

```python
# run.py
def startGame(self):
    self.setBackground()
    self.nodes = NodeGroup()
    self.nodes.setupTestNodes()
    self.pacman = Pacman(self.nodes.nodeList[0])
```
