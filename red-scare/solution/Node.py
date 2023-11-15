class Node:
    def __init__(self, id, is_red):
        self.id = id
        self.is_red = is_red

    def __repr__(self):
        return f"Node({self.id}, {self.is_red})"