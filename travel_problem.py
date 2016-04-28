from solver_utils import *
from common import *

class TravelProblemAction(Action):
    def __init__(self, from_city, to_city, cost):
        super(TravelProblemAction, self).__init__(to_city, cost)
        self.from_city = from_city
        self.to_city = to_city

    def __str__(self):
        return "Going from {} to {} (cost: {})".format(self.from_city, self.to_city, self.cost)

class TravelProblemState:
    def __init__(self, city_name):
        self.city_name = city_name

    def __str__(self):
        return self.city_name

    def __repr__(self):
        return self.city_name

    def __eq__(self, other):
        if isinstance(other, TravelProblemState):
            return self.city_name == other.city_name
        return NotImplemented
 
    def __hash__(self):
        return hash(self.city_name)

class City:
    def __init__(self, city_name, h_val, actions):
        self.state = TravelProblemState(city_name)
        self.h_val = h_val
        self.actions = actions

class TravelProblem(Problem):
    def __init__(self, target_city):
        super(TravelProblem, self).__init__(TravelProblemState(target_city), TravelProblemState("Bucharest"))
        self.cities = cities
        self.target_city = target_city
        self.maximum_depth = 100

    def succ_f(self, state):
        return [SuccFResult(action, TravelProblemState(action.to_city)) for action in self.cities[state.city_name].actions]

    def h(self, node):
        return self.cities[node.state.city_name].h_val

    def __str__(self):
        return self.target_city

def formulate_travel_problem(target_city):
    return TravelProblem(target_city)

cities = {
    "Arad": City("Arad", 366, [
        TravelProblemAction("Arad", "Zerind", 75),
        TravelProblemAction("Arad", "Sibiu", 140),
        TravelProblemAction("Arad", "Timisoara", 118)
    ]),
    "Zerind": City("Zerind", 374, [
        TravelProblemAction("Zerind", "Arad", 75),
        TravelProblemAction("Zerind", "Oradea", 71)
    ]),
    "Oradea": City("Oradea", 380, [
        TravelProblemAction("Oradea", "Sibiu", 151),
        TravelProblemAction("Oradea", "Zerind", 71)
    ]),
    "Timisoara": City("Timisoara", 329, [
        TravelProblemAction("Timisoara", "Arad", 118),
        TravelProblemAction("Timisoara", "Lugoj", 111)
    ]),
    "Lugoj": City("Lugoj", 329, [
        TravelProblemAction("Lugoj", "Timisoara", 111),
        TravelProblemAction("Lugoj", "Mehadia", 70)
    ]),
    "Mehadia": City("Mehdadia", 329, [
        TravelProblemAction("Mehadia", "Lugoj", 70),
        TravelProblemAction("Mehadia", "Dobreta", 75)
    ]),
    "Dobreta": City("Dobreta", 242, [
        TravelProblemAction("Dobreta", "Mehadia", 75),
        TravelProblemAction("Dobreta", "Craiova", 120)
    ]),
    "Craiova": City("Craiova", 160, [
        TravelProblemAction("Craiova", "Dobreta", 120),
        TravelProblemAction("Craiova", "Riminicu Vilcea", 146),
        TravelProblemAction("Craiova", "Pitesti", 138)
    ]),
    "Riminicu Vilcea": City("Riminicu Vilcea", 193, [
        TravelProblemAction("Riminicu Vilcea", "Sibiu", 80),
        TravelProblemAction("Riminicu Vilcea", "Pitesti", 97),
        TravelProblemAction("Riminicu Vilcea", "Craiova", 146)
    ]),
    "Pitesti": City("Pitesti", 100, [
        TravelProblemAction("Ptiesti", "Riminicu Vilcea", 97),
        TravelProblemAction("Ptiesti", "Craiova", 138),
        TravelProblemAction("Ptiesti", "Bucharest", 101)
    ]),
    "Fagaras": City("Fagaras", 176, [
        TravelProblemAction("Fagaras", "Sibiu", 99),
        TravelProblemAction("Fagaras", "Bucharest", 211)
    ]),
    "Sibiu": City("Sibiu", 253, [
        TravelProblemAction("Sibiu", "Arad", 140),
        TravelProblemAction("Sibiu", "Oradea", 151),
        TravelProblemAction("Sibiu", "Fagaras", 99),
        TravelProblemAction("Sibiu", "Riminicu Vilcea", 80),
    ]),
    "Bucharest": City("Bucharest", 0, [
        TravelProblemAction("Bucharest", "Fagaras", 211),
        TravelProblemAction("Bucharest", "Pitesti", 101),
        TravelProblemAction("Bucharest", "Giurgiu", 90),
        TravelProblemAction("Bucharest", "Urziceni", 85),
    ]),
    "Giurgiu": City("Giurgiu", 77, [
        TravelProblemAction("Giurgiu", "Bucharest", 90)
    ]),
    "Urziceni": City("Urziceni", 80, [
        TravelProblemAction("Urziceni", "Bucharest", 85),
        TravelProblemAction("Urziceni", "Hirsova", 98),
        TravelProblemAction("Urziceni", "Vaslui", 142)
    ]),
    "Vaslui": City("Vaslui", 199, [
        TravelProblemAction("Vaslui", "Iasi", 92),
        TravelProblemAction("Vaslui", "Urziceni", 142),
    ]),
    "Iasi": City("Iasi", 226, [
        TravelProblemAction("Iasi", "Neamt", 87),
        TravelProblemAction("Iasi", "Vaslui", 92),
    ]),
    "Neamt": City("Neamt", 234, [
        TravelProblemAction("Neamt", "Iasi", 87)
    ]),
    "Hirsova": City("Hirsova", 151, [
        TravelProblemAction("Hirsova", "Urziceni", 98),
        TravelProblemAction("Hirsova", "Eforie", 86)
    ]),
    "Eforie": City("Eforie", 161, [
        TravelProblemAction("Eforie", "Hirsova", 86),
    ])
}
