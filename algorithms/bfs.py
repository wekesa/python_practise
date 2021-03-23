# Breadth First Search

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict()

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, " ")
            # Get all adjacent vertices of the
            # de-queued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)



"""
Breadth First Search is an algorithm used for tree traversal on graphs or tree data structures.
BFS can easily ne implemented using recursion and data structures such as dictionaries and lists.
Algorithm:
1. Pick any node visit adjacent unvisited vertex, mark it as visited, display it and insert it in a queue
2. If there are no remaining adjacent vertices left, remove the first vertex from the queue 
3. Repeat step 1 and 2 until the queue is empty or the desired node is found
"""

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []

# Time complexity is O(V+E)
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)