# Write your solution here
def factorials(n: int):
    fact_dictionary = {}
    fact_dictionary[1] = 1
    for i in range(2, n + 1):
        fact_dictionary[i] = i * fact_dictionary[i-1]
    return fact_dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])