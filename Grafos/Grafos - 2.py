from sys import stdin
import math
import queue

WHITE = "white"
GRAY = "gray"
BLACK = "black"

class GraphL:
    def __init__(self, vertexes, arcs):
        self.V = set(vertexes)
        self.E = {}
        for arc in arcs:
            if arc[0] in self.E.keys():
                self.E[arc[0]].append(arc[1])
            else:
                self.E[arc[0]] = [arc[1]]

    def printArcs(self):
        for key in self.E.keys():
            print(key, self.E[key])

    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        return self.E[v] if v in self.E.keys() else []

    def initializeNode(self, v):
        return {
            'value': v,
            'color': WHITE,
            'distance': math.inf,
            'phi': None
        }

    def printBFS(self, bfsResult):
        for key in bfsResult.keys():
            print(key, bfsResult[key])

    def BFS(self, s):
        vertexesDic = {}
        Q = queue.Queue()
        for v in self.V:
            vertexesDic[v] = self.initializeNode(v)
            if v == s :
                vertexesDic[v]['color'] = GRAY
                vertexesDic[v]['distance'] = 0

        Q.put(s)
        while Q.qsize() > 0:
            element = Q.get()
            objE = vertexesDic[element]
            for neighbor in self.getNeighbors(element):
                obj = vertexesDic[neighbor]
                if obj['color'] == WHITE:
                    vertexesDic[neighbor]['color'] = GRAY
                    vertexesDic[neighbor]['distance'] = objE['distance'] + 1
                    vertexesDic[neighbor]['phi'] = element
                    Q.put(neighbor)
            vertexesDic[element]['color'] = BLACK
        return vertexesDic

class Graph:
    def __init__(self, vertexes, arcs):
        self.V = set(vertexes)
        self.E = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
        for arc in arcs:
            self.E[arc[0]][arc[1]] = 1
    

    def printArcs(self):
        for e in self.E:
            print(''.join(map(str,e)))

    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        neighbors = []
        candidates = self.getArcs()[v]
        for index in range(len(self.V)):
            if candidates[index] == 1:
                neighbors.append(index)
        return neighbors


def main():
    n,m = map(int, stdin.readline().strip().split())
    arcs = []
    vertexes = [x for x in range(n)]
    for i in range(m):
        arcs.append(list(map(int, stdin.readline().strip().split())))
    graph = Graph(vertexes, arcs)
    print("====================================== Matriz de adjacencias ===============================")
    graph.printArcs()
    print("====================================== Listas de adjacencias ===============================")
    graph2 = GraphL(vertexes, arcs)
    graph2.printArcs()
    print(graph2.printBFS(graph2.BFS(0)))
    print(graph2.printBFS(graph2.BFS(2)))


main()
"""
5 5
0 1
0 2
1 4
2 3
3 4
"""
