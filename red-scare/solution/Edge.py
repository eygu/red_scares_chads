class Edge:
    def __init__(self, weight, is_red, node_u, node_v):
        self.weight = weight
        self.is_red = is_red
        self.node_u = node_u
        self.node_v = node_v

    def __repr__(self):
        return f"Edge({self.weight}, {self.is_red}, {self.node_u}, {self.node_v})"