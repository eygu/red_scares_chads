from collections import defaultdict
import heapq
from heapq import heappop as pop, heappush as push

class G:
    def __init__(self, size):
        self.G = [defaultdict(int) for _ in range(size)]

    def add_edge(self, src, dest, weight, is_red):
        self.G[src][dest] = (weight, is_red)

    def dijkstra2(self, start, finish):
        N = len(self.G)
        dist = [float('inf')] * N
        pq = []
        def add(i, dst):
            if dst < dist[i]:
                dist[i] = dst
                push(pq, (dst, i))
        add(start, 0)

        while pq:
            D, i = pop(pq)
            if i == finish:
                print(dist)
                return D
            if D != dist[i]: continue
            for j, node_value in  self.G[i].items():
                is_red = node_value[1]
                w = node_value[0]
                if not is_red:
                    add(j, D + w)
        print(dist)
        return dist[finish]

def read_red_scare_data(filename):
    with open(filename, 'r') as file:
        n, m, r = map(int, file.readline().split())
        s, t = map(int, file.readline().split())

        graph = G(n)

        black_nodes = []
        red_nodes = []
        edges = []

        for i in range(n):
            line = file.readline().strip()
            is_red = line.endswith(" *")
            if is_red:
                red_nodes.append(int(line.rstrip(" *")))
            else:
                black_nodes.append(int(line.rstrip(" *")))

        for i in range(m):
            edge_str = file.readline().strip()
            if "--" in edge_str:
                u, v = map(int, edge_str.split(" -- "))
                if v not in red_nodes:
                    graph.add_edge(u, v, 1, False)
                    edges.append((u, v, False))
                else:
                    graph.add_edge(u, v, 1, True)
                    edges.append((u, v, True))

    return n, m, r, s, t, black_nodes, red_nodes, edges, graph

def main1():
    graph = G(10)

    graph.add_edge(0, 1, 10, False)
    graph.add_edge(0, 2, 10, False)
    graph.add_edge(0, 3, 10, True)
    graph.add_edge(1, 3, 10, False)

    print(graph)

def case_none(s, t, black_nodes, red_nodes, graph):
    if s in red_nodes:
        return -1
    if t in red_nodes:
        return -1
    return graph.dijkstra2(s, t)


def main():
    n, m, r, s, t, black_nodes, red_nodes, edges, graph = read_red_scare_data("C:/Gitprojects/Algorithm_Design-Assignments/red-scare/data/gnm-10-15-0.txt")

    res = case_none(s, t, black_nodes, red_nodes, graph)
    print(res)

if __name__ == "__main__":
    main()


