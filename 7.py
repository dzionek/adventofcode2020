import re
import networkx as nx
from typing import List

file = open('inputs/7.txt')
data = file.read().split('\n')
input_node = 'shiny gold bag'

parent_pattern = re.compile(r'^[^ ]+ [^ ]+ bag')
children_pattern = re.compile(r'\d+ [^ ]+ [^ ]+ bag')
adjacency = {}
for line in data:
    parent = parent_pattern.findall(line)[0]
    children = children_pattern.findall(line)
    if not children:
        adjacency[parent] = None
    else:
        children = [
            (child.partition(" ")[2], int(child.partition(" ")[0]))
            for child in children
        ]
        adjacency[parent] = children

G = nx.DiGraph()
for parent, children in adjacency.items():
    if children:
        for child in children:
            G.add_edge(parent, child[0], weight=child[1])

# Part A
print(len(nx.algorithms.ancestors(G, input_node)))

# Part B
input_node_descendants = nx.algorithms.descendants(G, input_node)
paths_to_descendants = [
    nx.all_simple_paths(G, input_node, descendant)
    for descendant in input_node_descendants
]

def find_path_weight(path: List[str]) -> int:
    i, j = 0, 1
    res = 1
    for _ in range(len(path) - 1):
        edge = (path[i], path[j])
        res *= G.get_edge_data(*edge)['weight']
        i += 1
        j += 1

    return res


print(sum([
    find_path_weight(path)
    for paths in paths_to_descendants for path in paths
]))
