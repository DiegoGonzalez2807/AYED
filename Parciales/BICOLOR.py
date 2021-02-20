from sys import stdin
from collections import deque
import math
class Initialize_vertex:
    def __init__(self, value):
        self.value = value
        self.distance = -math.inf
        self.color = 'White'
        self.bicolor = ""

class Graph:
    def __init__(self, n, arcs):
        self.nodes = [Initialize_vertex(x) for x in range(n)]
        self.arcs = arcs


def BFS(graph, source):
    new_graph = graph.nodes[source]
    new_graph.distance,new_graph.color,new_graph.bicolor, is_bicolorable = 0, 'Gray', "Red", True
    operation = deque()
    operation.append(new_graph)
    while operation:
        principal = operation.popleft()
        for value in graph.arcs[principal.value]:
            neighbor = graph.nodes[value]
            if neighbor.color == 'White':
                neighbor.d = principal.distance + 1
                neighbor.color = 'Gray'
                if principal.bicolor != "Red":
                    neighbor.bicolor = "Red"
                else:
                    neighbor.bicolor = "Blue"
                operation.append(neighbor)
            else:
                is_bicolorable = is_bicolorable and neighbor.bicolor != principal.bicolor
                if not is_bicolorable:
                    break
            principal.color = 'Black'
    return is_bicolorable



def main():
    while True:
        nodes = int(stdin.readline().strip())
        if nodes == 0:
            break
        connections = int(stdin.readline().strip())
        arcs = [[] for i in range(nodes)]
        for i in range(connections):
            a,b = list(map(int,stdin.readline().strip().split()))
            arcs[a].append(b)
            arcs[b].append(a)
        graph = Graph(nodes, arcs)
        answer = BFS(graph, 0)
        if answer:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

main()
