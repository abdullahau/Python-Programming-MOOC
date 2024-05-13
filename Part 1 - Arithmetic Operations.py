#| Operator      | Purpose                          | Example     | Result|
#|:-------------:|----------------------------------|-------------|-------|
#| `+`           | Addition                         | `2 + 4`     |`6`    |
#| `-`           | Subtraction                      | `10 - 2.5`  |`7.5`  |
#| `*`           | Multiplication                   | `-2 * 123`  |`-246` |
#| `/`           | Division (floating point result) | `9 / 2`     | `4.5` |
#| `//`          | Division (integer result)        | `9 // 2`    | `4`   |
#| `%`           | Modulo                           | `9 % 2`     |`1`    |
#| `**`          | Exponentiation                   | `2 ** 3`    |`8`    |

# data type of an operand and the type of the operator usually determines the data type of the result
# if a single one of the operands in an expression is a floating point number, the result will also be a floating point number, regardless of the other operands.
# Division always results in a floating point number, regardless of the other operands

height = 172.5 # in centimetres
weight = 68.55

# the Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
# height is converted into metres in the formula
bmi = weight / (height / 100) ** 2

print(f"The BMI is {bmi}")


# Integer division operator // -> Results are rounded down to the nearest integer

x = 3
y = 2

print(f"/ operator {x/y}")
print(f"// operator {x//y}")

# Casting strings and floats

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}")

# Commonly used shorthand notations that operate on variables in place. 
# Convenient way to add a value to an existing variable and assign the new value back to the same variable.
# sum = sum + number
# sum += number -> equivelent to sum = sum + number
# product = product * number
# product *= number -> equivelent to product = product * number
# difference = difference - number
# difference -= number -> equivelent to difference = difference - number


# Example 1
product = 1 # this is used to reset or initialize the product variable before each new calculation

number = int(input("Please type in the first number: "))
product *= number

number = int(input("Please type in the second number: "))
product *= number

number = int(input("Please type in the thurd number: "))
product *= number

print("The product is", product)

# Example 2
sum = 0 # this is ued to reset or initialize the sum variable before each new calculation

number = int(input("First number: "))
sum += number

number = int(input("Second number: "))
sum += number

number = int(input("Third number: "))
sum += number

print(f"The sum of the numbers: {sum}")

# Example 3
n = 0
n += int(input("Number 1: "))
n += int(input("Number 2: "))
n += int(input("Number 3: "))
n += int(input("Number 4: "))
print(f"The sum of the numbers is {n} and the mean is {n/4}")

# Example 4
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
print(f"The sum of the numbers: {n1 + n2}")
print(f"The product of the numbers: {n1 * n2}")

# Example 5
cafe_weekly = int(input("How many times a week do you eat at the student cafeteria? "))
avg_price = float(input("The price of a typical student lunch? "))
grocery_weekly = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {((cafe_weekly * avg_price) + grocery_weekly)/7} euros")
print(f"Weekly: {(cafe_weekly * avg_price) + grocery_weekly} euros")

# Example 6 - Students in a group -> Using '//' to round up instead of round down
students = int(input("How many students on the course? "))
desired_group = int(input("Desired group size? "))

print(f"Number of groups formed: {-(-students // desired_group)}")

# Example 6 - Students in a group - Approach 2
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
 
groups = (students + group_size - 1) // group_size
 
print("Number of groups formed:", groups)

# Round Up Division Methods
# rounded_up = -(-numerator // denominator)
# rounded_up = (numerator + denominator - 1) // denominator
# int(numerator / denominator) + (numerator % denominator > 0)