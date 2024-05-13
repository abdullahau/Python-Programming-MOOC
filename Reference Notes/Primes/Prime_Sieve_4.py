import time
import numpy as np

start = time.time()

limit = 1_000_000

prime_array = np.arange(2, limit+1)
i = 0

while True:
    try:
        prime = prime_array[i]
    except IndexError:
        break
    prime_comp = np.arange(prime, limit+1, prime)
    prime_array = np.setdiff1d(prime_array, prime_comp[1:])
    i += 1

end = time.time()

print("The time of execution of above program is :", (end-start), "s")


with open("1m_prime_sive_v0.txt", "w") as f:
    f.write("\n".join(map(str, prime_array)))

end2 = time.time()

print("The time of execution of above program is :", (end2-end), "s")