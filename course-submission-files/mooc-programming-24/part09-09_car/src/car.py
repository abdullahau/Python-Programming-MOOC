# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self) -> None:
        self.__fuel = 0
        self.__odometer = 0
    
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__fuel} litres"
    
    def fill_up(self) -> None:
        self.__fuel = 60
            
    def drive(self, km:int) -> None:
        if km <= self.__fuel and km > 0:
           self.__odometer += km
           self.__fuel -= km 
        elif km > self.__fuel and km > 0:
            self.__odometer += self.__fuel
            self.__fuel = 0

if __name__ == "__main__":
    car = Car()
    car.fill_up()
    car.drive(10)
    car.drive(20)
    car.drive(10)
    car.drive(20)
    print(car)