# Write your solution here
import json

class Player:
    def __init__(self, player: str, team: str, country: str, goals: int, assists: int, games: int) -> None:
        self.player = player
        self.team = team
        self.country = country
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
        self.games = games
        
    def __repr__(self) -> str:
        return f"{self.player: <21}{self.team: ^3}{self.goals: >4}{'+': ^3}{self.assists: >2}{'=': ^3}{self.points:>3}"


class FileProcessing:
    def __init__(self, filename: str):
        with open(filename, "r") as f:
            self.__jsondata = json.loads(f.read())
        
        self.__data = []
        for entry in self.__jsondata:
            self.__data.append(Player(entry["name"], entry["team"], entry["nationality"], entry["goals"], entry["assists"], entry["games"]))
    
    @property        
    def data(self) -> list:
            return self.__data

class Search:
    def __init__(self, filename) -> None:
        stats = FileProcessing(filename)
        self.data = stats.data
    
    def total_entries(self) -> int:
        return len(self.data)
    
    def player_search(self, name: str):
        player = list(filter(lambda x: x.player == name, self.data))
        return player[0]
    
    def teams(self):
        teams_list = list(set(map(lambda x: x.team, self.data)))
        teams_list.sort()
        return teams_list
    
    def countries(self):
        countries_list = list(set(map(lambda x: x.country, self.data)))
        countries_list.sort()
        return countries_list
    
    def team_search(self, team: str):
        team_list = list(filter(lambda x: x.team == team, self.data))
        team_list.sort(key=lambda x: x.points, reverse=True)
        return team_list
    
    def country_search(self, country: str):
        country_list = list(filter(lambda x: x.country == country, self.data))
        country_list.sort(key=lambda x: x.points, reverse=True)
        return country_list
    
    def most_points(self):
        most_points = sorted(self.data, key=lambda x: (x.points, x.goals), reverse=True)
        return most_points
    
    def most_goals(self):
        most_goals = sorted(self.data, key=lambda x: (x.goals, -x.games), reverse=True)
        return most_goals


class HockeyApplication:
    def __init__(self) -> None:
        pass
    
    def help(self) -> str:
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
        
    def execute(self):
        data = Search(input("file name: "))
        print(f"read the data of {data.total_entries()} players")
        self.help()
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                name = input("name: ")
                print(data.player_search(name))
            elif command == 2:
                teams = data.teams()
                for team in teams:
                    print(team)
            elif command == 3:
                countries = data.countries()
                for country in countries:
                    print(country)
            elif command == 4:
                team = input("team: ")
                team = data.team_search(team)
                for player in team:
                    print(player)
            elif command == 5:
                country = input("country: ")
                country = data.country_search(country)
                for player in country:
                    print(player)
            elif command == 6:
                number = int(input("how many: "))
                most_points = data.most_points()
                for i in range(number):
                    print(most_points[i])
            elif command == 7:
                number = int(input("how many: "))
                most_points = data.most_goals()
                for i in range(number):
                    print(most_points[i])

run = HockeyApplication()
run.execute()