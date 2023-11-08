import os

# Get all .txt files in the 'data' directory
files = [f for f in os.listdir('data') if f.endswith('.txt')]

graphs = []
# Load graphs from files
for file in files:
    with open(os.path.join('data', file), 'r') as f:
        lines = f.readlines()
        n, m, r = map(int, lines[0].split())
        s, t = lines[1].split()
        vertices = []
        edges = []
        for i in range(2, 2 + n):
            vertices.append(lines[i].strip())
        for i in range(2 + n, 2 + n + m):
            edges.append(tuple(lines[i].strip().split(' -- ')) if ' -- ' in lines[i] else tuple(lines[i].strip().split(' -> ')))
        graphs.append({
            'n': n,
            'm': m,
            'r': r,
            's': s,
            't': t,
            'vertices': vertices,
            'edges': edges
        })


# print(graphs[1])