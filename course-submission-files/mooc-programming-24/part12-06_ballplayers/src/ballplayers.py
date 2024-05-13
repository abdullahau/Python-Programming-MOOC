class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here

def most_goals(players: list) -> str:
    return max(players, key=lambda player: player.goals).name

def most_points(players: list) -> tuple:
    selected_player = max(players, key=lambda player: (player.goals + player.passes))
    return (selected_player.name, selected_player.number)

def least_minutes(players: list) -> BallPlayer:
    return min(players, key=lambda player: player.minutes)