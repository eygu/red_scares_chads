from collections import defaultdict
from heapq import heappop as pop, heappush as push

class UDG:
    def __init__(self, size, G, nodes, edges):
        self.size = size
        self.G = G
        self.nodes = nodes
        self.edges = edges

    def dijkstra(self, start, finish):
        N = len(self.G)
        dist = [float('inf')] * N
        pq = [(0, start)]

        nodes = self.nodes
        edges = self.edges

        while pq:
            curr_dist, u = pop(pq)
            if curr_dist > dist[u]:
                continue

            for v, weight in self.G[u].items():
                new_dist = curr_dist + weight
                if not nodes[v].is_red and new_dist < dist[v]:
                    dist[v] = new_dist
                    push(pq, (new_dist, v))
                
        return -1 if dist[finish] == float('inf') else dist[finish]

    
    def __repr__(self):
        return f"UDG({self.G})"



    