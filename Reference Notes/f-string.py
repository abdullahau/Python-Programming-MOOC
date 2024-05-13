# Commas and underscore for thousand seperator

n: int = 100_000_000

print(n)

n: float = 1e8

print(n)

n: int = 100000000

print(f'{n: _}') # underscore seperator

print(f'{n: ,}') # comma seperator

# Alignment & whitespaces

var: str = 'var'

print(f'{var: >20}:') # right align - take up 20 character spaces

print(f'{var: <20}:') # left align - take up 20 character spaces 

print(f'{var: ^20}:') # center align - take even spaces on either side for total of 20 character spaces


print(f'{var:_>20}:') # right align - add specified character instead of whitespace

print(f'{var:#<20}:') # left align - add specified character instead of whitespace

print(f'{var:|^20}:') # center align - add specified character instead of whitespace

# Date Time Formatting

from datetime import datetime

now: datetime = datetime.now()

print(f'{now:%d.%m.%y}')

print(f'{now:%d.%m.%y (%H:%M:%S)}')

print(f'{now:%c}') # system format

print(f'{now:%I%p}')

# Rounding 

n: float = 1234.5678

print(f'{n: .2f}') # Two decimal places

print(f'{n: .1f}') # One deicaml place

print(f'{n: .0f}') # Rounded to integer

print(f'{n:,.3f}') # Three decimal places with comma thousand seperator 

print(f'{n:_.2f}') # Two decimal places with underscore thousand seperator 

# Showing operators and operand

a: int = 5
b: int = 10
my_var: str = 'Abdullah'
boolean: bool = True

print(f'{a + b}') # Shows the final result of a + b

print(f'a + b = {a + b}')

print(f'{a + b = }') # Shows the operators and operand and the final result

print(f'{my_var = }') # Shows the variable name and the string stored in variable reference

print(f'{boolean = }')

print(f'{bool(a) = }')
