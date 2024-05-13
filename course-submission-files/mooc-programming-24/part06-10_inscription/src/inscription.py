# Write your solution here
sign = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file, "w") as inscription:
    inscription.write(f"Hi {sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")