import sys
from travel_problem import *
from test_single import test_single

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_city = sys.argv[1]
        algorithm = SearchAlgorithm[sys.argv[2]] if len(sys.argv) > 2 else SearchAlgorithm.TREESEARCH
        strategy = SearchStrategy[sys.argv[3]] if len(sys.argv) > 3 else SearchStrategy.A_STAR
        problem = formulate_travel_problem(start_city)
        test_single(problem, algorithm, strategy)
    else:
        print("Not enough arguments!")

