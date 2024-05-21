# Vectors

## Vector Basics

Vectors are a data structure that's useful for storing information like position and velocity. A vector is something that describes both magnitude and direction.  In order to illustrate this idea imagine that you live in a city with a grid-based system. You're located at point A and you're trying to get to point B. You're new in town so you stop somebody on the street and ask them. The person tells you that you need to go 3 blocks East, then 4 blocks South. The person gave you two sets of information and each set of information contained a distance and a direction. One set was 3 blocks East, and the other set was 4 blocks South. This is all a vector is, it's really that simple. In this case the person gave you two vectors to follow. Notice that both pieces of each vector are necessary in order for you to reach your destination. If the person had just told you to go 3 blocks, then 4 blocks, you'd naturally want to know in which direction you should travel those distances. Likewise, if he had told you to go East, then South, you'd want to know how far to travel in each direction. Vectors require both a magnitude (or length) and a direction. You should also notice that the order in which he gave you the directions doesn't matter. He could have just as easily told you to go 4 blocks South first, then 3 blocks East. He could have also sent you in all sorts of directions before reaching your destination, so you can see that there are actually an infinite number of paths to travel from A to B.

![Vector_basic](https://img1.wsimg.com/isteam/ip/51f9eb68-183a-416f-aedc-5c476e4e4d1c/img1.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true)

## Vector Arithmetic

 It would have been a lot easier if you could just go straight to point B cutting across all of the blocks. This is always the shortest path and usually the one we're most interested in. But this vector isn't purely East and it isn't purely South. It's a combination of both of these directions. If we could use shorthand to describe this vector it would be **3E + 4S** for 3 blocks East and 4 blocks South. Don't let the addition symbol confuse you, this isn't like adding 2 + 2 where we get a single result. We can add vectors together as we'll see below, but we can't add orthogonal directions such as East and South so we keep them separated with the addition symbol. We can add same directions together like **3N + 5N = 8N** and if the directions are opposite each other then we can add them together as well like **4N + 6S = 2S**. Adding opposite directions is basically subtraction. We don't even need special symbols for South and West since South = -North and West = -East. Then it makes more sense how we got the previous result if we write it as **4N - 6N = -2N**.

![Vector_arithmetic](https://img1.wsimg.com/isteam/ip/51f9eb68-183a-416f-aedc-5c476e4e4d1c/img2.png/:/cr=t:0%25,l:0%25,w:100%25,h:100%25/rs=w:400,cg:true)

## Create vector.py

Start by creating a file called `vector.py`.  You can organize the code any way you want, but for this tutorial I'm just going to have all of the code in a single folder called 'Pacman'. What I will then do is create this `vector.py` file inside the 'Pacman' folder and then copy the following code to the file.

To start we import the math package so we can use some predefined math functions. Then we create the `Vector` class. The x and y variables should be easy to understand based on the explanation above. They are just the coordinates that the vector is pointing towards. The `thresh` variable will be explained below when we actually use it.

```python
# vector.py
import math

class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001
```

## Arithmetic Methods

These are the methods that will allow us to add and subtract vectors, as well as multiply and divide a vector by a scalar. Notice in our division code that we first need to check that we are not dividing by 0. Very important! Also when multiplying and dividing a vector by a scalar, order matters. Not in general, but just here. The scalar always has to be on the right side.  So something like `Vector2 * 5` and not `5 * Vector2`.

What's the difference between the **\_\_div\_\_** and the **\_\_truediv\_\_** methods?  It appears that the **\_\_truediv\_\_** just calls the **\_\_div\_\_** method, so what gives? Python 3 does away with the **\_\_div\_\_** method in favor of the **\_\_truediv\_\_** method and Python 2 uses the **\_\_div\_\_** method. That's really it. I'm trying to make this work for both Python 2 and Python 3.

```python
# vector.py
def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

def __sub__(self, other):
    return Vector2(self.x - other.x, self.y - other.y)

def __neg__(self):
    return Vector2(-self.x, -self.y)

def __mul__(self, scalar):
    return Vector2(self.x * scalar, self.y * scalar)

def __div__(self, scalar):
    if scalar != 0:
        return Vector2(self.x / float(scalar), self.y / float(scalar))
    return None

def __truediv__(self, scalar):
    return self.__div__(scalar)
```

## Equality Methods

These methods allow us to check for equality between two vectors. This is also where we use the thresh variable. In computer-land two values can be nearly equal like 2 and 2.00000000001. If we were doing scientific computing, then that difference could be significant. However, we aren't doing science and we need to be able to say that those two values are the same. So we do that by subtracting the two values and then seeing if it's less than our theshold value, which is just a really small number. So in our game the two vectors <3,4> is equal to <3.000004, 4.000001>.

```python
# vector.py
def __eq__(self, other):
    if abs(self.x - other.x) < self.thresh:
        if abs(self.y - other.y) < self.thresh:
            return True
    return False
```

We have two types of magnitude methods here. The '**magnitude**' method returns the actual length of the vector which requires a square root (which is why we had to import the math package). The '**magnitudeSquared**' method, however, is the one we'll use more often in our game. The reason is because it does not require us to take a square root. It's good practice to avoid taking the square root in your games whenever you can avoid it. If all you need to do is compare the length of two vectors, then comparing their length squared is just as valid as comparing their length. For example, if m and n are the lengths of two vectors and if m > n, then it's also true that m2 > n2.

```python
def magnitudeSquared(self):
    return self.x**2 + self.y**2

def magnitude(self):
    return math.sqrt(self.magnitudeSquared())
```

The **copy** method allows us to copy any vector so we get a new instance of it. The reason we want to do this is because of how Python stores its variables in memory. I'll explain more when we get to an example. The reasoning though is that we want to create a new instance of this object, then we can modify the new object without touching this object.

The last two methods are just nice to have. They just convert our vector into a tuple and an int tuple. They really just make code cleaner later.

```python
def copy(self):
    return Vector2(self.x, self.y)

def asTuple(self):
    return self.x, self.y

def asInt(self):
    return int(self.x), int(self.y)
```

## String Method

This method doesn't affect the functionality of the game or anything, it's really a convenience function so we can easily print out the vector. So let's say we create a vector with `v = Vector(3,4)`. Then we want to print out the vector at some point. Naturally we want to say something like: `print(v)`. However, at this point if you do that you'll get something like the following printed out: `<vector.Vector object at 0x03020F70>`

That's not terribly useful, it just tells you where that object is in memory. So if we include the following function we can tell the class how we want the printout of the objects to look. So now if we say `print(v)` we'll get the following: `<3, 4>`. That's a lot more useful, so this method is good to have especially for debugging. You can add a **\_\_str\_\_** method to all of your classes and have it output whatever you want.

```python
def __str__(self):
    return "<"+str(self.x)+", "+str(self.y)+">"
```
