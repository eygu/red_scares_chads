from read_files import read_all_files, read_graph
import os 

def case_none(s, t, graph):
    if graph.nodes[s].is_red or graph.nodes[t].is_red:
        return -1
    
    return graph.bfs_none(s, t)

def case_alternate(s, t, graph):
    return graph.bfs_alternate(s, t)


def main():
    # dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../instance-generators/handmade'
    dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../data'
    file = "wall-p-1.txt"
    path = rf"{dataDirectory}/{file}"
    n, m, r, s, t, graph = read_graph(path)
    print(graph)
    res_none = case_none(s, t, graph)
    res_alternate = case_alternate(s, t, graph)
    print(f"file: {file}, dijkstra result: {res_none}")
    print(f"file: {file}, bfs_alternate result: {res_alternate}")

if __name__ == "__main__":
    main()