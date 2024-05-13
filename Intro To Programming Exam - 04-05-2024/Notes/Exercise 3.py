def read_points():
    
    # final result summary list
    result = []

    # point comp - (win, loss, tie)
    points = (3, 0, 1)

    # opening & reading file
    with open("statistics.txt", "r") as f:
        file_line = 0
        for line in f:
            # print(line)
            line = line.strip().split(":")
            # print(line)
            team = line[0]
            # print(team)
            team_stat = line[1].split("-")
            # print(team_stat)
            file_line += 1
            score = 0
            for i in range(len(team_stat)):
                try:
                    score += int(team_stat[i]) * points[i]
                except ValueError:
                    raise ValueError(f"Invalid format in file: {file_line}")
            # print(score)
            result.append((team , score))
            # print(result)
                
    return result

result = read_points()
print(result)