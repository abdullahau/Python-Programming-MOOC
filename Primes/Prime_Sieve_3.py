limit = 10000

ints_to_limit = list(range(2,limit+1))

prime_numbers = []
composites = []
prime = 2

while True:
    prime_numbers.append(prime)
    prime_comp = list(range(prime, limit+1, prime))
    composites = list(set(composites + prime_comp))
    ints_to_limit = sorted(list(set(ints_to_limit) - set(composites)))
    try:
        prime = ints_to_limit[0]
    except IndexError:
        break

with open("1m_prime_sive.txt", "w") as f:
    f.write("\n".join(map(str, prime_numbers)))