# Write your solution here
attempt = 0

while True:
    pin = input("Pin: ")

    attempt += 1

    if pin == "4321":
        break
    else:
        print("Wrong")

if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")