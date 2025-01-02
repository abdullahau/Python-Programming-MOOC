'''
Circuitous, LLC -
An Advanced Circle Analytics Company
Summary: Toolset for New-Style Classes
1. Inherit from object().
2. Instance variables for information unique to an instance.
3. Class variables for data shared among all instances.
4. Regular methods need "self" to operate on instance data.
5. Class methods implement alternative constructors. They need "cls"
   so they can create subclass instances as well.
6. Static methods attach functions to class. They don't need
   either "self" or "cls".
   Static methods improve discoverability and require context to be specified.
7. A property() lets getter and setter methods be invoked automatically by
   attribute access. This allows Python classes to freely expose their
   instance variables.
8. The "__slots__" variable implements the Flyweight Design Pattern by
   suppressing instance dictionaries
9. The __method() is a class local reference, making sure the method refers
   to this class's method, not its childrens'.
10. Thread local calls use the double underscore. Gives subclasses the 
    freedom to override methods without breaking other methods.
'''

import math

class Circle(object): # new-style class
    'An advanced circle analytics toolkit'
    
    # flyweight design pattern suppresses the instance dictionary 
    __slots__ = ['diameter']
    version = '0.7' # class variable
    
    def __init__(self, radius):
        # init is not a constructor. It's job is to initialize the instance variables
        self.radius = radius # instance variables
    
    @property # convert dotted access to method calls
    def radius(self):
        return self.diameter / 2.0
    
    @radius.setter
    def radius(self, radius):
        'Radius of a circle'
        self.diameter = radius * 2.0
    
    def area(self):  # regular methods have 'self' as first argument
        # Given that the perimeter method is modified and used in a subclass, we use the double under to create a class local reference to ensure modified perimeter from subclass is not used
        p = self.__perimeter() 
        r = p / math.pi / 2.0
        return math.pi * r** 2.0  
    
    def perimeter(self):
        return 2.0 * math.pi * self.radius
    
    @classmethod  # Alternative constructor
    def from_bbd(cls, bbd): # use `cls` petermeter to support subclassing
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)  # return `cls(radius)` instead of `Circle(radius)` so subclasses are not suppressed

    @staticmethod  # Attach functions to classes - works without instantiating the class
    def angle_to_grade(angle): 
        # A standard method would require creating a new instance just to call a function which needs no 'self' variables or any information about the instance of a `Circle`
        # Adding this function inside the Circle class improves discoverability and ensures the function is used in the appropriate context
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0   # variables used here do not require information about the instance
    
    __perimeter = perimeter # Class local reference


class Tire(Circle):
    'Tires are circles with an odometer corrected perimeter'
    
    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25

if __name__ == "__main__":
    std = Circle(2)
    print('Radius of the Circle:', std.radius)
    print('Area of the Circle:', std.area())
    print('Perimeter of the Circle:', std.perimeter())

    print()
    new = Circle.from_bbd(25)
    print('Radius of the Circle:', new.radius)
    print('Area of the Circle:', new.area())
    print('Perimeter of the Circle:', new.perimeter())

    print()
    t = Tire.from_bbd(25)
    print('Radius of the Circle:', t.radius)
    print('Area of the Circle:', t.area())
    print('Perimeter of the Circle:', t.perimeter()) # This does not work if `classmethod` returns the class instance rather than `cls`

    print()
    t = Tire(15)
    print('Radius of the Circle:', t.radius)
    print('Area of the Circle:', t.area())
    print('Perimeter of the Circle:', t.perimeter())

    print()
    grade = Circle.angle_to_grade(30)
    print('Angle:', 30)
    print('Grade:', grade)
    print('Type:', type(grade))
