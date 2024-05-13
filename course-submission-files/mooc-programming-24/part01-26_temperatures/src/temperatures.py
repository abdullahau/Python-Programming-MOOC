# Write your solution here
fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32)/1.8

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")