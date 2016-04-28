import abc
from queue import PriorityQueue
from AutoNumber import AutoNumber
from common import *

INFINITY = float("inf")

class SearchAlgorithm(AutoNumber):
    """
    Enum for all search algorithms.
    """

    TREESEARCH = ()
    GRAPHSEARCH = ()
    RBFS = ()
    ITERATIVE_DEEPENING = ()

class SearchStrategy(AutoNumber):
    """
    Enum for all search strategies.
    """

    NONE = ()
    BREADTH_FIRST = ()
    UNIFORM_COST = ()
    DEPTH_FIRST = ()
    GREEDY_FIRST = ()
    A_STAR = ()

class Action:
    """
    Class which represents an action and saves its associated cost.
    """

    def __init__(self, action, cost):
        self.cost = cost
        self.action = action

    def __str__(self):
        return str(self.action)

class Node:
    """
    Class which represents a node in the problem search tree.
    """

    def __init__(self, state, parent, action, depth=0, pathCost=0, f=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.pathCost = pathCost
        self.f = f
        self.h = h

    def __str__(self):
        return "{} -> {} (h(n): {}; pc+h(n): {}, d: {})".format(self.action, self.state, self.h, self.f, self.depth)

    def __lt__(self, other):
        return 0

class Problem:
    """
    Class which represents an abstract problem. Concrete problems should inherit
    from this class.
    """

    def __init__(self, start_state, target_state):
        self.start_state = start_state
        self.target_state = target_state

    def is_goal(self, node):
        return node.state == self.target_state

    @abc.abstractmethod
    def succ_f(self, state):
        return NotImplemented

    @abc.abstractmethod
    def h(self, node):
        return NotImplemented

    def f(self, node):
        return node.pathCost + self.h(node)

class SuccFResult:
    """
    Objects of this class shall contain a result of the successor function: An
    action and the resulting state.
    """

    def __init__(self, action, state):
        self.action = action
        self.state = state

class Fringe:
    """
    A container for nodes. It supports different strategies for saving and
    retrieving the nodes in different orders.
    """

    def __init__(self, strategy):
        self.strategy = strategy
        # Either use a list or a priority queue
        if strategy == SearchStrategy.BREADTH_FIRST or strategy == SearchStrategy.DEPTH_FIRST:
            self.fringe = []
        elif strategy == SearchStrategy.UNIFORM_COST or \
                strategy == SearchStrategy.GREEDY_FIRST or \
                strategy == SearchStrategy.A_STAR:
            self.fringe = PriorityQueue()

    def print_contents(self):
        if DEBUG_V > 1:
            print ("current Fringe:")
            if isinstance(self.fringe, list):
                for item in fringe:
                    print ("   {}".format(item))
            elif isinstance(self.fringe, PriorityQueue):
                for i in range(len(self.fringe)):
                    print ("   {}".format(self.fringe.queue[i]))

    def insert(self, node):
        # Breadth first and depth first: simply append the node to the list
        if self.strategy == SearchStrategy.BREADTH_FIRST:
            self.fringe.append(node)
        elif self.strategy == SearchStrategy.DEPTH_FIRST:
            self.fringe.append(node)
        # Uniform cost: Set the priority to the pathCost
        elif self.strategy == SearchStrategy.UNIFORM_COST:
            self.fringe.put((node.pathCost, node))
        # Greedy first: Set the priority to the heuristic value
        elif self.strategy == SearchStrategy.GREEDY_FIRST:
            self.fringe.put((node.h, node))
        # A*: Set the priority to the pathCost + heuristic value
        elif self.strategy == SearchStrategy.A_STAR:
            self.fringe.put((node.f, node))

    def pop(self):
        # Breadth first: Pop the node from the beginning of the list
        if self.strategy == SearchStrategy.BREADTH_FIRST:
            return self.fringe.pop(0)
        # Depth first: Pop the node from the end of the list
        elif self.strategy == SearchStrategy.DEPTH_FIRST:
            return self.fringe.pop()
        # Other strategies: Get the value from the queue with the lowest
        # priority value
        elif self.strategy == SearchStrategy.UNIFORM_COST:
            return self.fringe.get()[1]
        elif self.strategy == SearchStrategy.GREEDY_FIRST:
            return self.fringe.get()[1]
        elif self.strategy == SearchStrategy.A_STAR:
            return self.fringe.get()[1]

    def extend(self, items):
        for item in items:
            self.insert(item)

    def empty(self):
        if isinstance(self.fringe, list):
            return self.fringe == []
        elif isinstance(self.fringe, PriorityQueue):
            return self.fringe.empty()
