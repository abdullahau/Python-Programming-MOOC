# Write your solution here
def dict_of_numbers():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            30, 40, 50, 60, 70, 80, 90]

    num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 
                'seventy', 'eighty', 'ninety']

    number_dict = {}

    for i in range(0, 100):
        if i not in num:
            number_dict[i] = f"{num_words[num.index(i // 10 * 10)]}-{num_words[num.index(i - (i // 10 * 10))]}"
        else:
            number_dict[i] = num_words[num.index(i)]
    
    return number_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])