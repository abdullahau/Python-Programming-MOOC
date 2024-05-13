# Write your solution here
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    
    # check length is 11
    if len(pic) != 11:
        return False
    
    # check dates & personal identifers are ints 
    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year_short = int(pic[4:6])
        identifier = int(pic[7:10])
    except ValueError:
        return False
    
    # check date ints form valid datetime format
    if pic[6] == "+":
        year_century = 1800
    elif pic[6] == "-":
        year_century = 1900
    elif pic[6] == "A":
        year_century = 2000
    else:
        return False
    
    try:
        birthdate = datetime(year_century + year_short, month, day)
    except ValueError:
        return False
    
    # check control character is valid 
    reference = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    num = int((f"{pic[0:2]}{pic[2:4]}{pic[4:6]}{pic[7:10]}"))
    index = num % 31
    if reference[index] == pic[10]:
        return True
    else:
        return False