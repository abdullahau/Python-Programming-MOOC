# Write your solution here

limit = int(input("Limit: "))
start = 1
sums = 1

while sums < limit:
    start += 1
    sums = sums + start

print(sums)