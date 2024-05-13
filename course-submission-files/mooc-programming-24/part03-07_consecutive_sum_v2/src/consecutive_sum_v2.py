# Write your solution here
limit = int(input("Limit: "))
start = 1
sums = 1
calculation = "The consecutive sum: 1"

while sums < limit:
    start += 1
    calculation += f" + {start}"
    sums = sums + start
 
calculation += f" = {sums}"
print(calculation)