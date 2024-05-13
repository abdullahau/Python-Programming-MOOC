# Write your solution here
def who_won(game_board: list):
    empty = 0
    player1 = 0
    player2 = 0
    for row in game_board:
        for i in row:
            if i == 2:
                player2 += 1
            elif i == 1:
                player1 += 1
            else:
                empty += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

if __name__ == "__main__":           
    go_board = [
    [1, 0, 0, 0, 1, 0, 2, 0, 0],
    [0, 0, 0, 1, 2, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 4],
    [0, 2, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 2, 1, 0],
    [1, 0, 1, 0, 1, 0, 2, 0, 0],
    [0, 0, 1, 1, 0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1]
    ]

    who_won(go_board)