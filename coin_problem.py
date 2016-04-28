from math import ceil
from solver_utils import *
from common import *

class CoinProblem(Problem):
    def __init__(self, money):
        super(CoinProblem, self).__init__(CoinProblemState(money), CoinProblemState(0))
        self.coin_options = [25, 10, 1]
        self.money = money
        self.maximum_depth = money+1

    def succ_f(self, state):
        return [SuccFResult(CoinProblemAction(option), CoinProblemState(state.money-option)) for option in self.coin_options if state.money-option >= 0]

    def h(self, node):
        successors = self.succ_f(node.state)
        if successors == []:
            return 0
        return int(ceil(min([ node.state.money/float(res.action.action) for res in successors ])))
        # return min([ node.state.money/float(res.action.action) for res in successors ])

    def __str__(self):
        return str(self.money)

class CoinProblemState:
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
    def __init__(self, coin):
        super(CoinProblemAction, self).__init__(coin, 1)

    def __str__(self):
        return "Taking {}".format(self.action)

def formulate_coin_problem(money):
    return CoinProblem(money)
