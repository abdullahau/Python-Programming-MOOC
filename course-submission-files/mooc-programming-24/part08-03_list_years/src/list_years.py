# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    sorted_years = [dates[i].year for i in range(len(dates))]
    sorted_years.sort()
    return sorted_years