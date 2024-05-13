# Write your solution here
from random import choice

def roll(die: str) -> int:
    die_dict = {}
    die_dict["A"] = [3, 3, 3, 3, 3, 6]
    die_dict["B"] = [2, 2, 2, 5, 5, 5]
    die_dict["C"] = [1, 4, 4, 4, 4, 4]
    return choice(die_dict[die])

def play(die1: str, die2: str, times: int) -> tuple:
    reference = ["die1_wins","die2_wins", "draws"]
    win_dict = {}
    win_dict["die1_wins"] = 0
    win_dict["die2_wins"] = 0
    win_dict["draws"] = 0    
    for i in range(times):
        rolli = [roll(die1), roll(die2)]
        if rolli.count(max(rolli)) > 1:
            win_dict["draws"] += 1
        else:
            winner = rolli.index(max(rolli))
            win_dict[reference[winner]] += 1
    return (win_dict["die1_wins"], win_dict["die2_wins"], win_dict["draws"])