import json
 
class Statistics:
    def __init__(self, players: list):
        self.__players = players
 
    def by_points(self,  p):
        return  p['goals'] + p['assists']
 
    def by_goals(self,  p):
        # if the numbe of goals is equal, less played games is better
        return (p['goals'], -p['games'])
 
    def player_data(self, name: str):
        for player in self.__players:
            if player['name'] == name:
                return player
 
        return None
 
    def countries(self):
        return sorted(list(set(p['nationality'] for p in self.__players )))
 
    def teams(self):
        return sorted(list(set(p['team'] for p in self.__players )))
 
    def players_in_team(self, team: str):
        players = [ p for p in self.__players if p['team'] == team]
        return sorted(players, key=self.by_points, reverse=True)
 
    def players_from_country(self, country: str):
        players = [ p for p in self.__players if p['nationality'] == country]
        return sorted(players, key=self.by_points, reverse=True)
 
    def most_points(self, countryra):
        players = sorted(self.__players, key=self.by_points, reverse=True)
        return players[0: countryra]
 
    def most_goals(self, countryra):
        players = sorted(self.__players, key=self.by_goals, reverse=True)
        return players[0: countryra]
 
class Application:
    def __init__(self):
        self.__statistics = None
 
    def instructions(self):
        instructions = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions)
 
    def f(self, p: dict):
        """
            helper method, which creates a string out of players formatted for output
        """
        points = p['goals'] + p['assists']
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
 
    def read_file(self):
        file_name = input("file: ")
        with open(file_name) as file:
            data = file.read()
 
        players = json.loads(data)
        print(f"read the data of {len(players)} players")
        self.__statistics = Statistics(players)
 
    def get_playes(self):
        name = input("name: ")
        player = self.__statistics.player_data(name)
        if player:
            print(self.f(player))
 
    def get_teams(self):
        for team in self.__statistics.teams():
            print(team)
 
    def get_countries(self):
        for country in self.__statistics.countries():
            print(country)
 
    def players_in_team(self):
        team = input("team: ")
        for player in self.__statistics.players_in_team(team):
            print(self.f(player)) 
 
    def players_from_country(self):
        country = input("country: ")
        for player in self.__statistics.players_from_country(country):
            print(self.f(player)) 
 
    def most_points(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_points(number):
            print(self.f(player)) 
 
    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__statistics.most_goals(number):
            print(self.f(player)) 
 
    def execute(self):
        self.read_file()
        self.instructions()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.get_playes()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
 
Application().execute()