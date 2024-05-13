# Write your solution here
def filter_solutions():
    with open("solutions.csv") as calculations:
        correct_list = []
        incorrect_list = []
        for line in calculations:
            line = line.strip()
            parts = line.split(";")
            result = int(parts[2])
            if parts[1].find("+") > 0:
                index = parts[1].find("+")
                operand1 = parts[1][:index]
                operand2 = parts[1][index+1:]
                correct = int(operand1) + int(operand2)
            if parts[1].find("-") > 0:
                index = parts[1].find("-")
                operand1 = parts[1][:index]
                operand2 = parts[1][index+1:]
                correct = int(operand1) - int(operand2)
            row = []
            if result == correct:
                for part in parts:
                    row.append(part)
                correct_list.append(row)
            else:
                for part in parts:
                    row.append(part)
                incorrect_list.append(row)

    with open("correct.csv", "w") as my_file:
        for result in correct_list:
            line = ""
            for value in result:
                line += f"{value};"
            line = line[:-1]
            my_file.write(line+"\n")
            
    with open("incorrect.csv", "w") as my_file:
        for result in incorrect_list:
            line = ""
            for value in result:
                line += f"{value};"
            line = line[:-1]
            my_file.write(line+"\n")

if __name__ == "__main__":
    filter_solutions()
    filter_solutions()
    filter_solutions()