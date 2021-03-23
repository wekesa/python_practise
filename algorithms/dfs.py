# Problem solving skills
# Understanding the problem
# Design
# algorithms and data structure
# reversing a string without inbuilt methods
#
#
#
# Algorithm
# Inputs - string (Characters)
# Output - reversed string (Reversed characters)
# start
# var input_string
# var output_string
# for i in input_string:
#
#
#


def reverse_string(input_string):
    index = len(input_string)
    reversed_string = []
    while index > 0:
        reversed_string += input_string[index - 1]
        index -= 1
    print(reversed_string)


if __name__ == '__main__':
    example_string = "ajdhjfabjdakdjfh"
    reverse_string(example_string)



# DFS in python
"""
DFS is an algorithm for graph traversal. It can be implemented easily using recursion and data structures such as 
dictionaries and sets.

Algorithms Steps:
- Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes
- Repeat until all the nodes are visited, or the node to be searched is found.
-

Implementation:
- Consider this graph
graph = {
    "A": ['B', 'C'], 
    "B": ['D', 'E'],
    "C": ['F'],
    "D": [],
    "E": ['F'],
    "F": []
}

"""
graph = {
    "A": ['B', 'C'],
    "B": ['D', 'E'],
    "C": ['F'],
    "D": [],
    "E": ['F'],
    "F": []
}

visited = set() # Set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, "A")