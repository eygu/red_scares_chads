from Node import Node
from UDG import UDG
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
        else:
            is_word = False
            s, t = int(s), int(t)

        nodes = dict()
        edges = []
        G = [defaultdict(int) for _ in range(n)]
        word_to_idx = dict()

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
            else:
                nodes[i] = Node(i, is_red)

        print(nodes)

        for i in range(m):
            edge_str = file.readline().strip()
            if "--" in edge_str:
                if is_word:
                    u1, v1 = edge_str.split(" -- ")
                    u = word_to_idx[u1]
                    v = word_to_idx[v1]
                else:
                    u1, v1 = map(int, edge_str.split(" -- "))
                    u = nodes[u1].id
                    v = nodes[v1].id

                G[u][v] = 1
                G[v][u] = 1
            elif "->" in edge_str:
                if is_word:
                    u1, v1 = edge_str.split(" -- ")
                    u = word_to_idx[u1]
                    v = word_to_idx[v1]
                else:
                    u1, v1 = map(int, edge_str.split(" -- "))
                    u = nodes[u1].id
                    v = nodes[v1].id

                G[u][v] = 1

        graph = UDG(n, G, nodes, edges)

    return n, m, r, s, t, graph, word_to_idx, is_word