# Write your solution here
cafe_weekly = int(input("How many times a week do you eat at the student cafeteria? "))
avg_price = float(input("The price of a typical student lunch? "))
grocery_weekly = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {((cafe_weekly * avg_price) + grocery_weekly)/7} euros")
print(f"Weekly: {(cafe_weekly * avg_price) + grocery_weekly} euros")