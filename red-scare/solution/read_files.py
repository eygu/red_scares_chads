from Node import Node
from Edge import Edge
from Graph import Graph
import os
from collections import defaultdict

def read_all_files(dir_path):
    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res


def read_graph(filename):
    with open(filename, 'r') as file:
        is_word = False 
        is_grid = False
        is_wall = False
        is_ski = False
        is_increasing = False

        n, m, r = map(int, file.readline().split())
        s, t = file.readline().split()
        if s == "begin" and t == "ender":
            is_word = True
        elif s == "0_0":
            is_grid = True
        elif "wall" in filename:
            is_wall = True
        else:
            s, t = int(s), int(t)

        nodes = dict()
        G = [defaultdict(int) for _ in range(n)]

        word_to_idx = dict()
        grid_to_idx = dict()

        # Go through all the nodes
        for i in range(n):
            line = file.readline().strip()
            is_red = line.endswith(" *")
            if is_word:
                id = line[:-2] if is_red else line
                nodes[i] = Node(id, is_red)
                word_to_idx[id] = i
            elif is_grid:
                id = id = line[:-2] if is_red else line
                nodes[i] = Node(id, is_red)
                grid_to_idx[id] = i
            elif is_wall:
                nodes[i] = Node(i, is_red)
            else:
                nodes[i] = Node(i, is_red)

        print(nodes)

        # Go through all the edges
        for i in range(m):
            edge_str = file.readline().strip()
            if "--" in edge_str:
                if is_word:
                    u1, v1 = edge_str.split(" -- ")
                    u = word_to_idx[u1]
                    v = word_to_idx[v1]
                elif is_grid:
                    u1, v1 = edge_str.split(" -- ")
                    u = grid_to_idx[u1]
                    v = grid_to_idx[v1]
                elif is_wall:
                    u1, v1 = map(int, edge_str.split(" -- "))
                    u = nodes[u1].id
                    v = nodes[v1].id
                else:
                    u1, v1 = map(int, edge_str.split(" -- "))
                    u = nodes[u1].id
                    v = nodes[v1].id

                G[u][v] = 1
                G[v][u] = 1
            elif "->" in edge_str:
                if is_word:
                    u1, v1 = edge_str.split(" -> ")
                    u = word_to_idx[u1]
                    v = word_to_idx[v1]
                elif is_grid:
                    u1, v1 = edge_str.split(" -> ")
                    u = grid_to_idx[u1]
                    v = grid_to_idx[v1]
                elif is_wall:
                    u1, v1 = map(int, edge_str.split(" -> "))
                    u = nodes[u1].id
                    v = nodes[v1].id
                else:
                    u1, v1 = map(int, edge_str.split(" -> "))
                    u = nodes[u1].id
                    v = nodes[v1].id

                G[u][v] = 1

        graph = Graph(n, G, nodes)
        s, t = get_source_target(word_to_idx, grid_to_idx, is_word, is_grid, s, t)

    return n, m, r, s, t, graph


def read_graph_for_few(filename):
    with open(filename, 'r') as file:
        is_word = False 
        is_grid = False
        is_wall = False
        is_ski = False
        is_increasing = False

        n, m, r = map(int, file.readline().split())
        s, t = file.readline().split()
        if s == "begin" and t == "ender":
            is_word = True
        elif s == "0_0":
            is_grid = True
        elif "wall" in filename:
            is_wall = True
        else:
            s, t = int(s), int(t)

        nodes = dict()
        edges = []
        G = [defaultdict(int) for _ in range(n)]

        word_to_idx = dict()
        grid_to_idx = dict()

        # Go through all the nodes
        for i in range(n):
            line = file.readline().strip()
            is_red = line.endswith(" *")
            if is_word:
                id = line[:-2] if is_red else line
                nodes[i] = Node(id, is_red)
                word_to_idx[id] = i
            elif is_grid:
                id = id = line[:-2] if is_red else line
                nodes[i] = Node(id, is_red)
                grid_to_idx[id] = i
            elif is_wall:
                nodes[i] = Node(i, is_red)
            else:
                nodes[i] = Node(i, is_red)

        print(nodes)

        # Go through all the edges
        for i in range(m):
            edge_str = file.readline().strip()
            if "--" in edge_str:
                if is_word:
                    u1, v1 = edge_str.split(" -- ")
                    u = word_to_idx[u1]
                    v = word_to_idx[v1]
                elif is_grid:
                    u1, v1 = edge_str.split(" -- ")
                    u = grid_to_idx[u1]
                    v = grid_to_idx[v1]
                elif is_wall:
                    u1, v1 = map(int, edge_str.split(" -- "))
                    u = nodes[u1].id
                    v = nodes[v1].id
                else:
                    u1, v1 = map(int, edge_str.split(" -- "))
                    u = nodes[u1].id
                    v = nodes[v1].id

                if nodes[v].is_red:
                    e1 = Edge(1, True, u, v)
                    e2 = Edge(0, False, v, u)
                    G[u][v] = e1
                    G[v][u] = e2
                elif nodes[u].is_red:
                    e1 = Edge(0, False, u, v)
                    e2 = Edge(1, True, v, u)
                    G[u][v] = e1
                    G[v][u] = e2
                else:
                    e1 = Edge(0, False, u, v)
                    e2 = Edge(0, False, v, u)
                    G[u][v] = e1
                    G[v][u] = e2
                edges.append(e1)
                edges.append(e2)
                
            elif "->" in edge_str:
                if is_word:
                    u1, v1 = edge_str.split(" -> ")
                    u = word_to_idx[u1]
                    v = word_to_idx[v1]
                elif is_grid:
                    u1, v1 = edge_str.split(" -> ")
                    u = grid_to_idx[u1]
                    v = grid_to_idx[v1]
                elif is_wall:
                    u1, v1 = map(int, edge_str.split(" -> "))
                    u = nodes[u1].id
                    v = nodes[v1].id
                else:
                    u1, v1 = map(int, edge_str.split(" -> "))
                    u = nodes[u1].id
                    v = nodes[v1].id

                if nodes[v].is_red:
                    e1 = Edge(1, True, u, v)
                    G[u][v] = e1
                else:
                    e1 = Edge(0, False, u, v)
                    G[u][v] = e1
                
                edges.append(e1)

        graph = Graph(n, G, nodes)
        s, t = get_source_target(word_to_idx, grid_to_idx, is_word, is_grid, s, t)

    return n, m, r, s, t, graph

def get_source_target(word_to_idx, grid_to_idx, is_word, is_grid, s, t):
    if is_word:
        source = word_to_idx[s]
        target = word_to_idx[t]

    elif is_grid:
        source = grid_to_idx[s]
        target = grid_to_idx[t]
    
    else:
        source = s
        target = t

    return source, target
