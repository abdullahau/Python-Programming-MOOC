# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observations = []
    
    def add_observation(self, observation: str) -> None:
        self.__observations.append(observation)
    
    def latest_observation(self):
        if len(self.__observations) != 0:
            return self.__observations[-1]
        else:
            return ""
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self) -> str:
        return f"{self.__name}, {len(self.__observations)} observations"

