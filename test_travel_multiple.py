from travel_problem import *
from test_multiple import test_multiple

if __name__ == "__main__":
    test_cities = ["Arad", "Lugoj", "Iasi", "Riminicu Vilcea", "Hirsova"]
    test_multiple([formulate_travel_problem(city) for city in test_cities], "results_travel.html")

