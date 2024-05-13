# Write your solution to exercise 3 here
def read_points():
    
    # final result summary list
    result = []

    # point comp - (win, loss, tie)
    points = (3, 0, 1)

    # opening & reading file
    with open("statistics.txt", "r") as f:
        file_line = 0
        for line in f:
            line = line.strip().split(":")
            team = line[0]
            team_stat = line[1].split("-")
            file_line += 1
            score = 0
            for i in range(len(team_stat)):
                try:
                    score += int(team_stat[i]) * points[i]
                except ValueError:
                    raise ValueError(f"Invalid format in file: {file_line}")
            result.append((team , score))
                
    return result

if __name__ == "__main__":
    result = read_points()
    print(result)