from math import ceil
from solver_utils import *
from common import *

class CoinProblem(Problem):
    """
    Defines the coin exchange problem:
    A given ammount of money shall be exchanged using only a given set of coin
    options, using as few coins as possible.
    """

    def __init__(self, money):
        super(CoinProblem, self).__init__(CoinProblemState(money), CoinProblemState(0))
        self.coin_options = [25, 10, 1]
        self.money = money
        # Maximum depth that any search algorithm should search for a solutions.
        # Using more coins than the ammount of cents does not make sense.
        self.maximum_depth = money+1

    def succ_f(self, state):
        """
        The successor function. Returns SuccFResult objects containing
        possible actions and the resulting states for a given state.
        """
        return [SuccFResult(CoinProblemAction(option), CoinProblemState(state.money-option)) for option in self.coin_options if state.money-option >= 0]

    def h(self, node):
        """
        The heuristic function which estimates the required costs from the state
        of the current node to the target state (here 0 cents).
        """
        successors = self.succ_f(node.state)
        if successors == []:
            return 0
        # Calculates a rough estimate of the required coins to reach the target
        # state (always less than the real required coins)
        return int(ceil(min([ node.state.money/float(res.action.action) for res in successors ])))
        # return min([ node.state.money/float(res.action.action) for res in successors ])

    def __str__(self):
        return str(self.money)

class CoinProblemState:
    """
    Defines a state inside the problem (here a given ammount of remaining money
    to be exchanged).
    """

    def __init__(self, money):
        self.money = money

    def __str__(self):
        return "Remaining: "+str(self.money)

    def __repr__(self):
        return str(self.money)

    def __eq__(self, other):
        if isinstance(other, CoinProblemState):
            return self.money == other.money
        return NotImplemented
 
    def __hash__(self):
        return hash(self.money)

class CoinProblemAction(Action):
    """
    Defines a possible action. Here: Taking a given coin.
    """

    def __init__(self, coin):
        super(CoinProblemAction, self).__init__(coin, 1)

    def __str__(self):
        return "Taking {}".format(self.action)

def formulate_coin_problem(money):
    """
    Returns a new CoinProblem object for a given ammount of money.
    """
    return CoinProblem(money)
