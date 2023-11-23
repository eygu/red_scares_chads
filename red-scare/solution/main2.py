from read_files import read_all_files, read_graph, read_graph_for_few, read_graph_for_some2
import os 
from Flow import Flow
from Node import Node
from collections import defaultdict

def case_none(s, t, graph):
    if graph.nodes[s].is_red or graph.nodes[t].is_red:
        return -1
    
    return graph.bfs_none(s, t)

def case_alternate(s, t, graph):
    return graph.bfs_alternate(s, t)

def case_few(s, t, graph):
    return graph.dijkstra_few(s, t)

def case_some(source, finish, graph):
    red_nodes = graph.red_nodes
    sink_idx = len(graph.G)
    sink = Node(sink_idx, False)
    graph.nodes[sink_idx] = sink

    for red_node in red_nodes:
        print(red_node)
        flow = Flow(graph.G)
        flow.G.append(defaultdict(int))
        flow.increase_capacity(red_node, sink_idx, 2)
        res = flow.max_flow(source, sink_idx)
        if res == 2:
            return True
        
    return False    

def main_some():
    # dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../data'
    dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../instance-generators/handmade'
    file = "P3-1.txt"
    path = rf"{dataDirectory}/{file}"
    n, m, r, source, finish, graph = read_graph_for_some2(path)
    print(case_some(source, finish, graph))

def main():
    # dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../instance-generators/handmade'
    dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../data'
    # file = "wall-p-1.txt"
    file = "common-1-250.txt"
    path = rf"{dataDirectory}/{file}"
    n, m, r, s, t, graph = read_graph(path)
    n1, m1, r1, s1, t1, graph1 = read_graph_for_few(path)
    print("graph", graph)
    print("graph1", graph1)

    res_none = case_none(s, t, graph)
    res_alternate = case_alternate(s, t, graph)
    res_few = case_few(s1, t1, graph1)
    print(f"file: {file}, bfs_none result: {res_none}")
    print(f"file: {file}, bfs_alternate result: {res_alternate}")
    print(f"file: {file}, dijkstra_few result : {res_few}")

if __name__ == "__main__":
    #main()
    main_some()