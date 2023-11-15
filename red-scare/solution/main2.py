from read_files import read_all_files, read_graph
import os 

def case_none(s, t, graph, word_to_idx, is_word):
    if is_word:
        s = word_to_idx[s]
        t = word_to_idx[t]

    if graph.nodes[s].is_red or graph.nodes[t].is_red:
        return -1
    
    return graph.dijkstra(s, t)

def main():
    # path = r"/Users/williamforbrigd/dev/itu/01/algorithmdesign/red_scares_chads/red-scare/data"
    # file = "rusty-1-17.txt"

    dataDirectory =  os.path.dirname(os.path.realpath(__file__)) + '/../data'
    file = "grid-5-0.txt"
    path = rf"{dataDirectory}/{file}"
    n, m, r, s, t, graph, word_to_idx, is_word = read_graph(path)
    res = case_none(s, t, graph, word_to_idx, is_word)
    print(f"file: {file}, dijkstra result: {res}")

if __name__ == "__main__":
    main()