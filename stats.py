from solver_utils import Node
from common import *

class Stats:
    def __init__(self):
        self.reset_stats()

    def stat_node_creation(self, nodes):
        if isinstance(nodes, Node):
            nodes = [nodes]
        self.created_nodes += len(nodes)
        self.calc_memory_usage()
        if DEBUG_V > 1:
            for node in nodes:
                print ("Creating node: {}".format(node))

    def stat_node_deletion(self, nodes):
        if isinstance(nodes, Node):
            nodes = [nodes]
        self.deleted_nodes += len(nodes)
        self.calc_memory_usage()
        if DEBUG_V > 1:
            for node in nodes:
                print ("Deleting node: {}".format(node))

    def stat_node_expansion(self, nodes):
        if isinstance(nodes, Node):
            nodes = [nodes]
        self.expanded_nodes += len(nodes)
        if DEBUG_V > 1:
            for node in nodes:
                print ("Expanding node: {}".format(node))

    def stat_node_ignoring(self, nodes):
        if isinstance(nodes, Node):
            nodes = [nodes]
        self.ignored_nodes += len(nodes)
        if DEBUG_V > 1:
            for node in nodes:
                print ("Ignoring node: {}".format(node))

    def calc_memory_usage(self):
        self.nodes_currenty_in_memory = self.created_nodes - self.deleted_nodes;
        self.max_nodes_concurrent_in_memory = max(self.max_nodes_concurrent_in_memory, self.nodes_currenty_in_memory)

    def reset_stats(self):
        self.expanded_nodes = 0
        self.created_nodes = 0
        self.deleted_nodes = 0
        self.ignored_nodes = 0
        self.max_nodes_concurrent_in_memory = 0
