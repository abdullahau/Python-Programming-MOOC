# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        entry = input("Diary entry: ")
        
        with open("diary.txt", "a") as diary:
            diary.write(f"{entry}\n")
        
        print("Diary saved")
    
    if function == 2:
        with open("diary.txt") as diary:
            print("Entries:")
            for line in diary:
                line = line.strip()
                print(line)
    
    if function == 0:
        print("Bye now!")
        break