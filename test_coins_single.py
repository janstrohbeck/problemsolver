import sys
from coin_problem import *
from test_single import test_single

if __name__ == "__main__":
    if len(sys.argv) > 1:
        money = int(sys.argv[1])
        algorithm = SearchAlgorithm[sys.argv[2]] if len(sys.argv) > 2 else SearchAlgorithm.TREESEARCH
        strategy = SearchStrategy[sys.argv[3]] if len(sys.argv) > 3 else SearchStrategy.A_STAR
        problem = formulate_coin_problem(money)
        test_single(problem, algorithm, strategy)
    else:
        print("Not enough arguments!")

