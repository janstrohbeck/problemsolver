from problemsolver import ProblemSolver

def test_single(problem, algorithm, strategy):
    print ("Algorithm: {}".format(algorithm.name))
    print ("Strategy: {}".format(strategy.name))

    print ("Starting search")

    solver = ProblemSolver()
    result = solver.search_problem_solution(problem, algorithm, strategy)

    print ("Finished search")
    stats = solver.get_stats()
    print ()
    print ("Expanded nodes: {}".format(stats.expanded_nodes))
    print ("Created nodes: {}".format(stats.created_nodes))
    print ("Deleted nodes: {}".format(stats.deleted_nodes))
    print ("Ignored nodes: {}".format(stats.ignored_nodes))
    print ("Max nodes concurrent in memory: {}".format(stats.max_nodes_concurrent_in_memory))
    print ()

    if result != None:
        print ("Resulting path:")
        for node in result:
            print ("  {}".format(node))
    else:
        print ("Did not find a solution!")
