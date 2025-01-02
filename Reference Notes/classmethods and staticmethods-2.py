# In essence most methods are instance methods and are designed to access instance data:
class CustomClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x_squared(self):
        return self.x ** 2

# self essentially means "this instance" and so:
this_instance = CustomClass(3, 4)

# When the method is called from the class, an instance needs to be supplied:
a = CustomClass.x_squared(self=this_instance)

# The method can then work on the instance data. Normally self is provided positionally. When a method is called from an instance, the instance is implied:
a = this_instance.x_squared()
# And therefore the instance data from this_instance will be used.

# The main use of a class method is an alternative constructor:
class CustomClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_inverse(cls, a, b):
        x = 1 / a
        y = 1 / b
        return CustomClass(x, y)

# This means a new CustomClass can be created using:
this_instance = CustomClass(x=3, y=4)

# Or the alternative constructor:
that_instance = CustomClass.from_inverse(a=1/3, b=1/3)

# Notice that the class method is called from the class and does not have an instance. 
# The class method can be called from an instance although it is not common to do so:
that_instance = this_instance.from_inverse(a=1/3, b=1/3)

# However all it does is determine the type of the class from the instance and invoke the class method and does not access instance data.
print(this_instance.y)
print(type(that_instance))

# the static method is neither bound to a class or a method.
# The static method is a regular function found in the namespace of a class and is only placed there for convenience. 
# Notice that it neither has self (an instance) or cls (a class) as the first input argument and is therefore not bound to an instance or a class:
class CustomClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def some_function(c, d):
        return c + d

test = CustomClass.some_function(3,5) 
print(type(test)) # test is not an instance of CustomClass. It is only a reference to the return value from the staticmethod
