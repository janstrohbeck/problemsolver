import abc
from queue import PriorityQueue
from AutoNumber import AutoNumber
from common import *

INFINITY = float("inf")

class SearchAlgorithm(AutoNumber):
    TREESEARCH = ()
    GRAPHSEARCH = ()
    RBFS = ()
    ITERATIVE_DEEPENING = ()

class SearchStrategy(AutoNumber):
    NONE = ()
    BREADTH_FIRST = ()
    UNIFORM_COST = ()
    DEPTH_FIRST = ()
    GREEDY_FIRST = ()
    A_STAR = ()

class Action:
    def __init__(self, action, cost):
        self.cost = cost
        self.action = action

    def __str__(self):
        return str(self.action)

class Node:
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
    def __init__(self, action, state):
        self.action = action
        self.state = state

class Fringe:
    def __init__(self, strategy):
        self.strategy = strategy
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
        if self.strategy == SearchStrategy.BREADTH_FIRST:
            self.fringe.append(node)
        elif self.strategy == SearchStrategy.DEPTH_FIRST:
            self.fringe.append(node)
        elif self.strategy == SearchStrategy.UNIFORM_COST:
            self.fringe.put((node.pathCost, node))
        elif self.strategy == SearchStrategy.GREEDY_FIRST:
            self.fringe.put((node.h, node))
        elif self.strategy == SearchStrategy.A_STAR:
            self.fringe.put((node.f, node))

    def pop(self):
        if self.strategy == SearchStrategy.BREADTH_FIRST:
            return self.fringe.pop(0)
        elif self.strategy == SearchStrategy.DEPTH_FIRST:
            return self.fringe.pop()
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
