from collections import defaultdict

class Node:
    def __init__(self, is_red, id):
        self.id = id
        self.is_red = is_red

    def __repr__(self):
        return self.id

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self, size):
        self.G = [defaultdict(Node) for _ in range(size)]

    def add_node(self, node):
        self.G[node]

    def add_edge(self, src, dest, weight):
        self.G[src][dest] = Edge(src, dest, weight)




if __name__ == "__main__":
    graph = Graph(10)

    graph.add_edge(0, 1, 10, False)
    graph.add_edge(0, 2, 10, False)
    graph.add_edge(0, 3, 10, True)
    graph.add_edge(1, 3, 10, False)

    print(graph)