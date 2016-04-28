from coin_problem import *
from problemsolver import ProblemSolver
import operator
import time
import sys

algo_combinations = [
    (SearchAlgorithm.TREESEARCH, [
        SearchStrategy.A_STAR,
        SearchStrategy.GREEDY_FIRST,
        SearchStrategy.DEPTH_FIRST,
        SearchStrategy.BREADTH_FIRST,
        SearchStrategy.UNIFORM_COST
    ]),
    (SearchAlgorithm.GRAPHSEARCH, [
        SearchStrategy.A_STAR,
        SearchStrategy.GREEDY_FIRST,
        SearchStrategy.DEPTH_FIRST,
        SearchStrategy.BREADTH_FIRST,
        SearchStrategy.UNIFORM_COST
    ]),
    (SearchAlgorithm.RBFS, [SearchStrategy.NONE]),
    (SearchAlgorithm.ITERATIVE_DEEPENING, [SearchStrategy.NONE])
]

def test_multiple(problems, results_filename="results.html"):
    with open(results_filename, "w") as f:
        print ("<html><head></head><body>", file=f)
        for problem in problems:
            print ("<table border=\"1\">", file=f)

            print ("Problem: {}".format(problem))

            print ("Problem: {}<br />".format(problem), file=f)
            print ("<tr>", file=f)
            print ("<th></th>", file=f)
            for algorithm, strategies in algo_combinations:
                print ("<th colspan=\"{}\">{}</th>".format(len(strategies), algorithm.name), file=f)
            print ("</tr>", file=f)

            print ("<tr>", file=f)
            print ("<th></th>", file=f)
            for algorithm, strategies in algo_combinations:
                for strategy in strategies:
                    if strategy != SearchStrategy.NONE:
                        print ("<th>{}</th>".format(strategy.name), file=f)
                    else:
                        print ("<th></th>", file=f)
            print ("</tr>", file=f)

            stats = []
            times = []
            costs = []
            for algorithm, strategies in algo_combinations:
                for strategy in strategies:
                    solver = ProblemSolver()

                    print ("  {}, {}: ".format(algorithm.name, strategy.name), end="")
                    sys.stdout.flush()
                    start_time = time.time()
                    result = solver.search_problem_solution(problem, algorithm, strategy)
                    time_delta = round(round(time.time() - start_time, 5) * 1000, 2)
                    s = solver.get_stats()
                    stats.append(s)
                    times.append(time_delta)
                    cost = 0
                    if result != None:
                        for node in result:
                            cost += node.action.cost
                    else:
                        cost = "No solution!"
                    costs.append(cost)
                    print ("{} ms".format(time_delta))

            def print_stat(f, name, stats, key=lambda x: x):
                print ("<tr>", file=f)
                print ("<td>{}</td>".format(name), file=f)
                for stat in stats:
                    print ("<td>{}</td>".format(key(stat)), file=f)
                print ("</tr>", file=f)

            stat_names = [
                ("expanded_nodes", "Expanded nodes"),
                ("created_nodes", "Created nodes"),
                ("deleted_nodes", "Deleted nodes"),
                ("ignored_nodes", "Ignored nodes"),
                ("max_nodes_concurrent_in_memory", "Max nodes concurrent in memory")
            ]

            for key, name in stat_names:
                print_stat(f, name, stats, key=lambda x: getattr(x, key))
            print_stat(f, "Execution time", [str(time)+" ms" for time in times])
            print_stat(f, "Solution Cost", costs)

            f.write("</table>")
            f.write("<br /><br />")

        f.write("</body></html>")

