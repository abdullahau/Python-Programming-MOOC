# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    with open(filename) as stations_data:
        station_dict = {}
        for line in stations_data:
            line = line.strip()
            part = line.split(";")
            if part[0] == "Longitude":
                continue
            station_dict[part[3]] = (float(part[0]), float(part[1]))
        return station_dict

def distance(stations: dict, station1: str, station2: str):
    for station, coordinates in stations.items():
        if station == station1:
            longitude1 = coordinates[0]
            latitude1 = coordinates[1]
        elif station == station2:
            longitude2 = coordinates[0]
            latitude2 = coordinates[1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = (x_km**2 + y_km**2)**(1/2)
    return distance_km

def greatest_distance(stations: dict):
    distance = 0 
    station_x = ""
    station_y = ""
    for station1, coordinates1 in stations.items():
        for station2, coordinates2 in stations.items():
            longitude1 = coordinates1[0]
            latitude1 = coordinates1[1]
            longitude2 = coordinates2[0]
            latitude2 = coordinates2[1]
            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = (x_km**2 + y_km**2)**(1/2)
            if distance_km > distance:
                distance = distance_km
                station_x = station1
                station_y = station2
    return station_x, station_y, distance


if __name__ == "__main__":
    stations = get_station_data("stations1.csv")

    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)