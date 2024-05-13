# Write your solution here
def week_error(week_lable):
    try:
        if week_lable[0:5] == "week " and int(week_lable[5:]) > 0:
            return True
    except ValueError:
        return False

def number_error(lottery_numbers):
    lottery_numbers = lottery_numbers.split(",")
    if len(lottery_numbers) == 7:
        number_list = []
        for number in lottery_numbers:
                try:
                    if int(number) >= 1 and int(number) <= 39 and number not in number_list:
                        number_list.append(number)
                    else:
                        return False
                except ValueError:
                    return False
        if len(number_list) == 7:
            return True
    else:
        return False

def filter_incorrect():
    with open("lottery_numbers.csv") as main, open("correct_numbers.csv", "w") as correct:
        for line in main:
            line = line.strip()
            parts = line.split(";")
            if week_error(parts[0]) and number_error(parts[1]):
                correct.write(line + "\n")