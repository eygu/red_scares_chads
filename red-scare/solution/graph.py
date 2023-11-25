from collections import defaultdict, deque
from heapq import heappop as pop, heappush as push
from G import G

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
    
    # Have all the edges that are red have weight 1 and the rest is 0
    def dijkstra_some(self, start, finish):
            N = len(self.G)
            dist = [float('inf')] * N
            pq = [(0, start)]

            nodes = self.nodes

            while pq:
                curr_dist, u = pop(pq)
                if curr_dist > dist[u]:
                    continue

                for v, edge in self.G[u].items():
                    new_dist = curr_dist + edge.weight
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        push(pq, (new_dist, v))
                    
            return True if dist[finish] > 0 else False
    

    def bfs_alternate(self, start, finish):
        visited = set()
        queue = deque([(start, [start])])

        nodes = self.nodes

        while queue:
            u, path = queue.popleft()
            
            if u == finish:
                return True
            
            if u not in visited:
                visited.add(u)
                for v, weight in self.G[u].items():
                    if v not in visited and nodes[u].is_red != nodes[v].is_red:
                        queue.append((v, path + [v]))

        return False

    def bfs_many(self, start, finish):
        if self.isCyclic():
            return -1
        #TODO: actually make the code
        return
    
    def __repr__(self):
        return f"Graph({self.G})"
    
    def isCyclicUtil(self, v, visited, recStack, path):
        visited[v] = True
        recStack[v] = True
        path.append(v)

        for neighbour in self.G.G[v].keys():
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack, path) == True:
                    return True
            elif recStack[neighbour] == True:
                # Cycle detected, print the path for reference
                print("Cycle detected:", path + [neighbour])
                return True

        recStack[v] = False
        path.pop()
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * len(self.nodes)
        recStack = [False] * len(self.nodes)
        for node in range(len(self.nodes)):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack, []) == True:
                    return True
        return False


if __name__ == '__main__':

    #Test graph with cycle
    g1 = G(5)
    g1.add_edge(0, 1, 1, False)
    g1.add_edge(1, 2, 1, False)
    g1.add_edge(2, 3, 1, False)
    g1.add_edge(3, 4, 1, False)
    g1.add_edge(4, 0, 1, False)

    graph1 = Graph(5, g1, [0, 1, 2, 3, 4])

    # Test graph without cycle
    g2 = G(6)
    g2.add_edge(0, 1, 1, False)
    g2.add_edge(0, 2, 1, False)
    g2.add_edge(1, 3, 1, False)
    g2.add_edge(2, 3, 1, False)
    g2.add_edge(3, 4, 1, False)
    g2.add_edge(4, 5, 1, False)

    graph2 = Graph(6, g2, [0, 1, 2, 3, 4, 5])

    # Test graph with multiple cycles 
    g3 = G(7)
    g3.add_edge(0, 1, 1, False)
    g3.add_edge(1, 2, 1, False)
    g3.add_edge(2, 0, 1, False)
    g3.add_edge(2, 3, 1, False)
    g3.add_edge(3, 4, 1, False)
    g3.add_edge(4, 2, 1, False)
    g3.add_edge(5, 6, 1, False)
    g3.add_edge(6, 5, 1, False)

    graph3 = Graph(7, g3, [0, 1, 2, 3, 4, 5, 6])

    if graph3.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")