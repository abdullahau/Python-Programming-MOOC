# Nodes

## Basics

Like I mentioned in the previous section, Pacman is currently able to move anywhere he wants to move. This isn't the kind of movement we want though. If you've played Pacman before, and I'm sure you have if you're reading this, then you know that he can only move around within a maze. So we need to figure out a way to constrain his movement. When I first wrote a Pacman game I did this by checking for wall collisions. I defined the maze to be a bunch of walls and checked if Pacman was colliding with the walls and basically just keeping him in between the walls. This may seem like a good solution, but it's not. I ran into a lot of issues that I won't discuss here, but I eventually thought of a way better method. That method is defining the maze as a map of connected nodes. That was a huge revelation for me and it solved all of the issues I was facing with collision detection. I'll go over what I mean by a "map of connected nodes" below and we'll generate a simple maze for Pacman to traverse as we're learning the basics of this.

Maybe you've studied data structures, but it's more than likely you haven't. That's fine, you don't need a degree in computer science to understand this stuff, I don't have one. Let's start off with defining what a Node is. A Node is really anything you want it to be. It's a very abstract thing. It's basically an abstract object that contains information. Usually when you're talking about nodes in video games, one of the most important pieces of information is the position of the node. You can also represent a node any way you like, we're going to represent a node as a red circle. Nodes by themselves aren't that interesting. They become way more interesting when you start linking them up together. When we have two nodes that are directly linked together we say that they are neighbors. Being a neighbor to any particular node has nothing to do with proximity. Two nodes can be right next to each other, but if they are not linked together, then they are not neighbors. If two nodes are connected to each other, then they are connected by a path. We'll represent a path by a straight line that joins two nodes together. That's how we can know visually that two nodes are connected to each other. When you have a bunch of nodes linked together in various ways, then that is called a node map. You've probably seen node maps before, they can be used in various ways. For example, representing a network of computers like the internet. Our node map that we'll make for our game will be a simplified version. The main restriction we'll place on our node map is that each node can only have a maximum of 4 neighbors. This is because Pacman can only move in four directions: `UP`, `DOWN`, `LEFT`, and `RIGHT`. So a node can be connected to four other nodes in those four directions. Also a node can only have a maximum of one neighbor in any one direction. By that I mean a node cannot be connected to two or more nodes to the `RIGHT` of him, for example. If he is connected to a node on his `RIGHT`, there can only be one node to his `RIGHT`.

![nodes_screen](https://img1.wsimg.com/isteam/ip/51f9eb68-183a-416f-aedc-5c476e4e4d1c/nodes.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true)

## Node Neighbors

The image on the right shows 7 nodes labeled A-G. These nodes are connected together with white lines that represent the paths between these nodes. As you can see node A has two neighbors: nodes B and C. Node D has three neighbors: nodes B, C, and E. The numbers on the edges show what row and column each node is in. Node B, for example is in row 2, column 4. We are going to write up some code in order to draw these nodes and their connections onto our screen.  

![nodes_grid](https://img1.wsimg.com/isteam/ip/51f9eb68-183a-416f-aedc-5c476e4e4d1c/node_basic.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true)

## More Colors

We need to add these to the **constants.py** file. RED will be the color of the nodes and WHITE will be the color of the paths between the nodes.

```python
# constants.py
WHITE = (255, 255, 255)
RED = (255, 0, 0)
```

## Node Class

In order to get some nodes up on the screen we'll start by creating a Node class. We'll create a file called **nodes.py** and add that class to it.

Start by putting in the three imports.

When we create a `Node` we pass in the row and column values and then compute the `x` and `y` position we want to place the Node on the screen. We also set up the neighbors as a dictionary. This way it's really easy to know which node is in which direction to this Node.

Then all we need to do is render the Node so it appears on the screen. We draw all of the paths to the neighbors first as `WHITE` lines, and we draw the Node itself as a `RED` circle. When we're finished with the game we don't actually draw the nodes, but we draw them now while we're developing the game.

```python
# node.py
import pygame
from vector import Vector2
from constants import *

class Node(object):
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None}

    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)
```

## NodeGroup Class

Having a Node class is great when dealing with individual nodes, but we're going to be dealing with a lot of nodes. It would be better if we grouped all of the nodes together so let's create another class in the nodes.py file where we actually create all of the individual nodes. This class needs to be placed after the Nodes class.

We're going to keep all of our Node objects in a list called nodeList, which starts out empty.

After we create our `NodeGroup` object we'll call a method called setupTestNodes which is just a temporary method we're using to show how we manually create and link up the nodes together. When creating each Node you need to pass in the location you want to place the Node in (row, column) format. Then, after the nodes have been created, we need to link them up together by adding nodes to the neighbors dictionary of each node. Finally, we add all of the nodes to the nodeList.

When we want to draw all of the nodes we call the render method which just loops through the nodeList and calls that nodes render method.

```python
# nodes.py
class NodeGroup(object):
    def __init__(self):
        self.nodeList = []

    def setupTestNodes(self):
        nodeA = Node(80 ,80)
        nodeB = Node(160, 80)
        nodeC = Node(80, 160)
        nodeD = Node(160, 160)
        nodeE = Node(208, 160)
        nodeF = Node(80, 320)
        nodeG = Node(208, 320)
        nodeA.neighbors[RIGHT] = nodeB
        nodeA.neighbors[DOWN] = nodeC
        nodeB.neighbors[LEFT] = nodeA
        nodeB.neighbors[DOWN] = nodeD
        nodeC.neighbors[UP] = nodeA
        nodeC.neighbors[RIGHT] = nodeD
        nodeC.neighbors[DOWN] = nodeF
        nodeD.neighbors[UP] = nodeB
        nodeD.neighbors[LEFT] = nodeC
        nodeD.neighbors[RIGHT] = nodeE
        nodeE.neighbors[LEFT] = nodeD
        nodeE.neighbors[DOWN] = nodeG
        nodeF.neighbors[UP] = nodeC
        nodeF.neighbors[RIGHT] = nodeG
        nodeG.neighbors[UP] = nodeE
        nodeG.neighbors[LEFT] = nodeF
        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)
```

Now that we have the `NodeGroup` class written we can create an instance of it in the GameController class. So make the following changes to the **run.py** file.

In order to use the `NodeGroup` class we'll need to import it first. Add this import to the top of the run.py file with the rest of the imports.

These two lines need to be added to the **startGame** method. Place them before creating the Pacman object. The order doesn't matter right now, but it will later.

Finally, we want to draw the nodes to the screen. Add this to the **render** method. The order in which you place things here matter. It depends if you want objects to appear on top or behind other objects. Place this code before drawing the Pacman object so that Pacman will appear in front of the nodes. But make sure you place it after drawing the black background, otherwise the background will cover the nodes and you'll think something is wrong since there won't be any nodes on the screen.

## GameController Class

```python
# run.py
from nodes import NodeGroup

def startGame(self):
    self.setBackground()
    self.nodes = NodeGroup()
    self.nodes.setupTestNodes()
    self.pacman = Pacman()

def render(self):
    self.screen.blit(self.background, (0,0))
    self.nodes.render(self.screen)
    self.pacman.render(self.screen)
    pygame.display.update()
```
