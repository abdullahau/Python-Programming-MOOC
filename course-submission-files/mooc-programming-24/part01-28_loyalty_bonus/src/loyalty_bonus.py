# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    bonus_rate = 1.1
    print("Your bonus is 10 %")

if points >= 100:
    bonus_rate = 1.15
    print("Your bonus is 15 %")

points *= bonus_rate 
print("You now have", points, "points")