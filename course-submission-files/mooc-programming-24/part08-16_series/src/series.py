# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rates = []
    
    def rate(self, rating: int):
        self.rates.append(rating)
        
    def __str__(self) -> str:
        if len(self.rates) > 0:
            average = sum(self.rates)/len(self.rates)
            rating = f"{len(self.rates)} ratings, average {average:.1f} points"
        else:
            rating = "no ratings"
            
        return f'{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{rating}'
    

def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if len(series.rates) > 0 and sum(series.rates)/len(series.rates) >= rating]

def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres] 