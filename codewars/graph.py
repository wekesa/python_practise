# Can be represented using a tuple
"""
- A graph is a data structure which consists of nodes which are connected by links.
- These nodes are called vertices while the links are called edges
- Operations that can be performed on graphs:
   - Display graph vertices
   - Display graph edges
   - Add a vertex
   - Add an edge
   - Creating a Graph

Graph can be created using a dictionary in python
"""
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_vertices(self):
        return list(self.gdict.keys())

    # Adding a vertex as a key
    def add_vertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    # Add an edge
    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]


graph = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

# Print the graph
print(graph)
