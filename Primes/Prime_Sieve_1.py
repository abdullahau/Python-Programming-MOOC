limit = 114

ints_to_limit = list(range(2,limit+1))

prime_numbers = []
composites = []
prime = 2

while True:
    prime_numbers.append(prime)
    for comp in ints_to_limit:
        if comp % prime == 0:
            composites.append(comp)
    ints_to_limit = sorted(list(set(ints_to_limit) - set(composites)))
    try:
        prime = ints_to_limit[0]
    except IndexError:
        break

for num in prime_numbers:
    print(num)