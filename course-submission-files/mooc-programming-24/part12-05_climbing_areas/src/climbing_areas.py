class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"

def sort_by_number_of_routes(areas: list):
    def order_by_routes(area: ClimbingArea):
        return area.routes()
    return sorted(areas, key=order_by_routes)

def sort_by_most_difficult(areas: list):
    def order_by_most_difficult(area: ClimbingArea):
        return area.hardest_route().grade
    return sorted(areas, key=order_by_most_difficult, reverse=True)
