from collections import defaultdict
from graph import Graph

def read_red_scare_data(filename):
    with open(filename, 'r') as file:
        n, m, r = map(int, file.readline().split())
        s, t = file.readline().split()


        graph = Graph(n)

        vertices = []
        edges = []

        for i in range(n):
            line = file.readline().strip()
            is_Red = line.endswith(" *")
            vertices.append((line.rstrip(" *"), is_Red))

        for i in range(m):
            edge_str = file.readline().strip()
            if "--" in edge_str:
                u, v = edge_str.split(" -- ")
                graph.add_edge(u, v, 1, )
                edges.append((u, v, False))
            elif "->" in edge_str:
                u, v = edge_str.split(" -> ")
                edges.append((u, v, True))

    return n, m, r, s, t, vertices, edges


if __name__ == "__main__":
    filename = "C:/Gitprojects/Algorithm_Design-Assignments/red-scare/data/common-1-100.txt"  # Replace with your input file name
    n, m, r, s, t, vertices, edges = read_red_scare_data(filename)

    print(f"n = {n}, m = {m}, r = {r}")
    print(f"s = {s}, t = {t}")

    # print("Vertices:")
    # for vertex, is_R in vertices:
    #     if is_R:
    #         print(f"{vertex} *")
    #     else:
    #         print(vertex)

    # print("Edges:")
    # for u, v, is_directed in edges:
    #    if is_directed:
    #        print(f"{u} -> {v}")
    #    else:
    #        print(f"{u} -- {v}")
