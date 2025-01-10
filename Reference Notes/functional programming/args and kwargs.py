# *args - arbitrary positional arguments - pass a variable number of positional arguments to a function. 
# Send a non-keyworded variable length argument list to the function. 

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
print()

def add(*nums): # usage '*args' is just a convention, it is not necessary to write *args. Only the * (asterisk) is necessary. 
    total = 0
    for i in nums:
        total += i
    print(f'Sum is {total}')

add(1,2) # values are passed as a tuple (immutable)
add(1,2,3,4,5)
add(1,2,3,4,5,-10,20,50)
print()

# **kwargs - keyworded arguments - pass keyworded variable length of arguments to a function. 
# You should use **kwargs if you want to handle named arguments in a function.
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

greet_me(name="Yasoob", age=20, nationality='American') # values are passed as a dictionary 
print()

def info_person(*args, **kwargs):
    total = 1
    for i in args:
        total *= i
    print(total)
    
    for key, value in kwargs.items():
        print(f'{key} = {value}')
        
info_person(1, 3, 4, 5, name='Abdullah', age=31)