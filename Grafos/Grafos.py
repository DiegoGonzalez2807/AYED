from sys import stdin
import math
import queue
#Colors
WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

class DFS:
    def __init__(self,vertexes, arcs):
        self.V = {}
        for v in vertexes:
            self.V[v] = self.initializeVertex()
        self.E = {}
        for v in self.V:
            self.E[v] = []

        for arc in arcs:
            self.E[arc[0]].append(arc[1])

    def initializeVertex(self):
        return {
            'color': WHITE,
            'distance': math.inf,
            'final_time': math.inf,
            'phi': None
        }

    def DFS_VISIT(self, u, time):
        time = time + 1
        self.V[u]['distance'] = time
        self.V[u]['color'] = GRAY
        for neighbor in self.getNeighbors(u):
            if self.V[neighbor]['color'] == WHITE :
                self.V[neighbor]['phi'] = u
                time = self.DFS_VISIT(neighbor, time)
        self.V[u]['color'] = BLACK
        self.V[u]['final_time'] = time + 1
        return time

    def DFS(self):
        for vertex in self.V.keys():
            self.V[vertex]['color'] = WHITE
            self.V[vertex]['phi'] = None
        time = 0
        for u in self.V.keys():
            if self.V[u]['color'] == WHITE:
                self.DFS_VISIT(u, time)
        return self.V

    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        return self.E[v]

    def printArcs(self):
        for v in self.E.keys():
            print(v, self.E[v])

    def matrix(self):
        matrix = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
        for v in self.E.keys():
            for i in self.E[v]:
                matrix[v][i] = 1
        for line in matrix:
            print(''.join(map(str,line)))




class BFS:
    def __init__(self,vertexes, arcs):
        self.V = {}
        for v in vertexes:
            self.V[v] = self.initializeVertex()
        self.E = {}
        for v in self.V:
            self.E[v] = []
        for arc in arcs:
            self.E[arc[0]].append(arc[1])

    def initializeVertex(self):
        return {
            'color': WHITE,
            'distance': math.inf,
            'final_time': math.inf,
            'phi': None
        }
    def BFS(self, s):
        for vertex in self.V.keys():
            self.V[vertex] = self.initializeVertex()
            if vertex == s:
                self.V[vertex]['color'] = GRAY
                self.V[vertex]['distance'] = 0
        Q = queue.Queue()
        Q.put(s)
        while Q.qsize() > 0:
            vertex = Q.get()
            vertexObj = self.V[vertex]
            for neighbor in self.getNeighbors(vertex):
                neighborObj = self.V[neighbor]
                if neighborObj['color'] == WHITE:
                    self.V[neighbor]['color'] = GRAY
                    self.V[neighbor]['distance'] = vertexObj['distance'] + 1
                    self.V[neighbor]['phi'] = vertex
                    Q.put(neighbor)
            self.V[vertex]['color'] = BLACK
        return self.V

    def printCurrentState(self, result):
        for vertex in result.keys():
            print(vertex, result[vertex])

    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        return self.E[v]

    def printArcs(self):
        for v in self.E.keys():
            print(v, self.E[v])

    def matrix(self):
        matrix = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
        for v in self.E.keys():
            for i in self.E[v]:
                matrix[v][i] = 1
        for line in matrix:
            print(''.join(map(str,line)))



class Graph:
    def __init__(self,vertexes, arcs):
        self.V = set(vertexes)
        self.E = [[ 0 for i in range(len(self.V))] for j in range(len(self.V))]
        for arc in arcs:
            self.E[arc[0]][arc[1]] = 1

    def getVertexes(self):
        return self.V

    def getArcs(self):
        return self.E

    def getNeighbors(self, v):
        neighbors = []
        candidates = self.E[v]
        for vertex in range(len(candidates)):
            if candidates[vertex] == 1:
                neighbors.append(vertex)
        return neighbors

    def printArcs(self):
        for line in self.E:
            print(''.join(map(str,line)))



'''
12 16
0 1
0 2
0 6
1 2
1 5
1 3
2 3
3 4
5 4
6 7
6 10
7 8
8 9
8 11
9 11
10 9
'''
