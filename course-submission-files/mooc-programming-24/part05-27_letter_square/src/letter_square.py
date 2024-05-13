# Write your solution here
layer = int(input("Layers: "))
width = (1 + (layer - 1) * 2 )

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

width_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
              29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]

index = layer
line = ""
index2 = 0
index3 = layer
fix = ""
inverted = []

for i in range(layer-1, -1, -1):
    for z in range(0, index2):
        fix += letters[index3]
        index3 -= 1
    line = fix + letters[index - 1] * width_list[index-1] + fix[::-1]
    print(line)
    inverted.append(line)
    line = ""
    fix = ""
    index -= 1
    index2 += 1
    index3 = layer - 1
for i in inverted[layer-2::-1]:
    print(i)