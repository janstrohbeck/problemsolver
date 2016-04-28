from coin_problem import *
from test_multiple import test_multiple

if __name__ == "__main__":
    test_money = [91, 92, 93, 94]
    test_multiple([formulate_coin_problem(money) for money in test_money], "results_coins.html")
