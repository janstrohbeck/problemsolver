from solver_utils import *
from common import *

class TravelProblem(Problem):
    """
    Defines the Romania travel problem:
    Finding the path with least costs from a given start city to Bucharest.
    """

    def __init__(self, start_city):
        """
        Initializes the instance with a given start city.
        """
        super(TravelProblem, self).__init__(TravelProblemState(start_city), TravelProblemState("Bucharest"))
        self.cities = cities
        self.start_city = start_city
        # Solving this problem should not require a depth of more than 100.
        self.maximum_depth = 100

    def succ_f(self, state):
        """
        The successor function. Returns SuccFResult objects containing
        possible actions and the resulting citys for the given city.
        """
        return [SuccFResult(action, TravelProblemState(action.to_city)) for action in self.cities[state.city_name].actions]

    def h(self, node):
        """
        The heuristic function which estimates the required costs from the state
        of the current node to the target state (here Bucharest).
        """
        return self.cities[node.state.city_name].h_val

    def __str__(self):
        return self.start_city

class TravelProblemState:
    """
    Defines a state inside the problem (here a given city).
    """

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

class TravelProblemAction(Action):
    """
    Defines a possible action. Here: Traveling from one city to another.
    """

    def __init__(self, from_city, to_city, cost):
        super(TravelProblemAction, self).__init__(to_city, cost)
        self.from_city = from_city
        self.to_city = to_city

    def __str__(self):
        return "Going from {} to {} (cost: {})".format(self.from_city, self.to_city, self.cost)

def formulate_travel_problem(start_city):
    """
    Returns a new TravelProblem object for a given start city.
    """

    return TravelProblem(start_city)

class City:
    """
    Class which saves information of a city.
    """

    def __init__(self, city_name, h_val, actions):
        # The associated state
        self.state = TravelProblemState(city_name)
        # The heuristic value
        self.h_val = h_val
        # The possible actions from this city
        self.actions = actions

# Definition of the cities, heuristics, actions and their costs.
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
