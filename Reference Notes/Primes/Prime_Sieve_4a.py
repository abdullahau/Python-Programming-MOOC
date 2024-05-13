import time
import numpy as np

start = time.time()

limit = 10_000_000

prime_array = np.arange(2, limit+1)

# Limit of composite building & crossing is set to a maximum of square root of limit
for i in range(0,round(limit**(1/2))):
    prime = prime_array[i]
    prime_comp = np.arange(prime**2, limit+1, prime)
    prime_array = np.setdiff1d(prime_array, prime_comp)

end = time.time()

print("The time of execution of above program is :", (end-start), "s")

with open("10m_prime_sive.txt", "w") as f:
    f.write("\n".join(map(str, prime_array)))

end2 = time.time()

print("The time of execution of above program is :", (end2-end), "s")


'''
Pseudocode:

algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i^2, i^2+i, i^2+(2i), i^2+(3i), ..., not exceeding n do
                set A[j] := false

    return all i such that A[i] is true.

# Limit of composite building & crossing is set to a maximum of square root of limit.
# All subequent numbers in the remaining list being analyzed will have an x^2 more than the limit
# Additionally all numbers after the square roof of limit shall have already had their multiples/composites prior to x^2 crossed from list

Example: 
11 * 1 - Include in prime
11 * 2 - crossed as composite
11 * 3 - crossed as composite
11 * 4 - crossed as composite
11 * 5 - crossed as composite
11 * 6 - crossed as composite
11 * 7 - crossed as composite
11 * 8 - crossed as composite
11 * 9 - crossed as composite
11 * 10 - crossed as composite
11 * 11 - Start 
11 * 12 
11 * 13
11 * 14 
11 * 15 
11 * 16 
11 * 17
11 * 18 
11 * 19
11 * 20 
11 * 21 
11 * 22 
11 * 23
'''
