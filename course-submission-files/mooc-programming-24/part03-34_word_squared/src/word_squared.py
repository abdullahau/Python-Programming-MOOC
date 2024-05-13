# Write your solution here
def squared(string, exp):
    
    string *= exp**2

    i = 0
    row = 0
    while row < exp:
        print(string[i : exp + i])
        i += exp
        row += 1
