from stats import Stats
from solver_utils import *
from common import *
from random import shuffle

class ProblemSolver:
    def __init__(self):
        self.stats = Stats()

    def search_problem_solution(self, problem, algorithm, strategy=SearchStrategy.NONE):
        if algorithm == SearchAlgorithm.TREESEARCH:
            strategy = strategy if strategy != SearchStrategy.NONE else SearchStrategy.A_STAR
            return self.treesearch(problem, strategy)

        elif algorithm == SearchAlgorithm.GRAPHSEARCH:
            strategy = strategy if strategy != SearchStrategy.NONE else SearchStrategy.A_STAR
            return self.graphsearch(problem, strategy)

        elif algorithm == SearchAlgorithm.RBFS:
            return self.RBFS(problem)

        elif algorithm == SearchAlgorithm.ITERATIVE_DEEPENING:
            return self.iterative_deepening(problem)

        return NotImplemented

    def expand(self, problem, pnode):
        successors = []
        self.stats.stat_node_expansion(pnode)
        for act_res in problem.succ_f(pnode.state):
            cnode = Node(act_res.state, pnode, act_res.action, pnode.depth+1, pnode.pathCost+act_res.action.cost)
            cnode.h = problem.h(cnode)
            cnode.f = problem.f(cnode)
            successors.append(cnode)
            self.stats.stat_node_creation(cnode)
        #shuffle(successors)
        return successors

    def path(self, root, node):
        path = []
        while node != root:
            if node == None:
                return None
            path.insert(0, node);
            node = node.parent
        return path

    def get_stats(self):
        return self.stats

    def treesearch(self, problem, strategy):
        root = Node(problem.start_state, None, Action(0, None))
        self.stats.stat_node_creation(root)
        
        fringe = Fringe(strategy)
        fringe.insert(root)
        while True:
            if fringe.empty():
                return None
            fringe.print_contents()

            currNode = fringe.pop()
            if (problem.is_goal(currNode)):
                return self.path(root, currNode)
            successors = self.expand(problem, currNode)
            if problem.maximum_depth > 0 and len([x for x in successors if x.depth > problem.maximum_depth]) > 0:
                return None
            fringe.extend(successors)

    def graphsearch(self, problem, strategy):
        root = Node(problem.start_state, None, Action(0, None))
        self.stats.stat_node_creation(root)
        fringe = Fringe(strategy)
        fringe.insert(root)
        closed = set([])
        while True:
            if fringe == []:
                return None
            fringe.print_contents()

            currNode = fringe.pop()

            if (problem.is_goal(currNode)):
                return self.path(root, currNode)

            if not currNode.state in closed:
                closed.add(currNode.state)

                successors = self.expand(problem, currNode)
                accepted_successors = [item for item in successors if not item.state in closed]
                rejected_successors = [item for item in successors if item.state in closed]
                self.stats.stat_node_deletion(rejected_successors)

                if problem.maximum_depth > 0 and len([x for x in accepted_successors if x.depth > problem.maximum_depth]) > 0:
                    return None
                fringe.extend(accepted_successors)
            else:
                self.stats.stat_node_ignoring(currNode)

    def RBFS(self, problem):
        def recursion(problem, cNode, cLimit):
            if problem.is_goal(cNode):
                return ([cNode], 0)

            successors = self.expand(problem, cNode)
            if successors == []:
                return (None, INFINITY)
            for node in successors:
                node.f = max(cNode.f, problem.f(node))

            while True:
                successors.sort(key=lambda x: x.f)
                best = successors[0]
                if best.f > cLimit:
                    self.stats.stat_node_deletion(successors)
                    return (None, best.f)
                limit = min(cLimit, successors[1].f) if len(successors) > 1 else cLimit
                rnl, rlim = recursion(problem, best, limit)
                if rnl != None:
                    rnl.insert(0, cNode)
                    return (rnl, 0)
                best.f = rlim

        root = Node(problem.start_state, None, Action(0, None))
        self.stats.stat_node_creation(root)
        return recursion(problem, root, INFINITY)[0][1:]

    def iterative_deepening(self, problem, max_depth=1):
        if max_depth > problem.maximum_depth:
            return None
        created_nodes_start = self.stats.created_nodes
        root = Node(problem.start_state, None, Action(0, None))
        fringe = Fringe(SearchStrategy.DEPTH_FIRST)
        fringe.insert(root)
        while True:
            if fringe.empty():
                break
            fringe.print_contents()

            currNode = fringe.pop()
            if (problem.is_goal(currNode)):
                return self.path(root, currNode)
            if currNode.depth <= max_depth:
                fringe.extend(self.expand(problem, currNode))
        self.stats.deleted_nodes += self.stats.created_nodes - created_nodes_start
        self.stats.calc_memory_usage()
        return self.iterative_deepening(problem, max_depth+1)
