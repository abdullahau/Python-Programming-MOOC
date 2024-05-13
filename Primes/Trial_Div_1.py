def prime_numbers():
    prime = 2
    printed_list = []
    while True:
        yield prime
        printed_list.append(prime)
        prime = max(printed_list) + 1
        i = 0
        while i < len(printed_list):
            if prime % printed_list[i] != 0:
                i += 1
            else:
                prime += 1
                i = 0

numbers = prime_numbers()
for i in range(30):
    print(next(numbers))