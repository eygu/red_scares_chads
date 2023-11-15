from collections import defaultdict, deque
from heapq import heappop as pop, heappush as push

class Graph:
    def __init__(self, size, G, nodes):
        self.size = size
        self.G = G
        self.nodes = nodes
    
    def bfs_none(self, start, finish):
        N = len(self.G)
        visited = set()
        queue = deque([(start, 0)])

        nodes = self.nodes

        while queue:
            u, curr_dist = queue.popleft()

            if u == finish:
                return curr_dist 

            if u not in visited:
                visited.add(u)
                for v, weight in self.G[u].items():
                    if not nodes[v].is_red:
                        queue.append((v, curr_dist + weight))

        return -1  # If no path is found

    def dijkstra_none(self, start, finish):
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
    

    def bfs_alternate(self, start, finish):
        visited = set()
        queue = deque([(start, [start])])

        nodes = self.nodes

        while queue:
            u, path = queue.popleft()
            
            if u == finish:
                print(path)
                return True
            
            if u not in visited:
                visited.add(u)
                for v, weight in self.G[u].items():
                    if v not in visited and nodes[u].is_red != nodes[v].is_red:
                        queue.append((v, path + [v]))

        return False

    
    def __repr__(self):
        return f"Graph({self.G})"



    