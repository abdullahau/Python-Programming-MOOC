# Write your solution here
wage_rate = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day_week = input("Day of the week: ")

if day_week == "Sunday":
    wage = wage_rate * 2 * hours
    print(f"Daily wages: {wage} euros")
if day_week != "Sunday":
    wage = wage_rate * hours
    print(f"Daily wages: {wage} euros")