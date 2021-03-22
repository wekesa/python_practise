# Dijkstra's Algorithm allows you to calculate the shortest path between one node
# of your choosing and every other node in a graph.

import sys


# Function to determine which vertex to be visited next
def to_be_visisted():
    global visited_and_distance
    v = -10
    # Choosing the Vertex with minimum distance
    for index in range(vertices_length):
        if visited_and_distance[index][0] == 0 and (v < 0 or visited_and_distance[index][1] <=visited_and_distance[v][1]):
            v = index
    return v


# Sample Graph using adjacency matrix
vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]

edges = [[0, 3, 4, 0],
         [0, 0, 0.5, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]

vertices_length = len(vertices[0])
# 1st element Indicates whether the node has been visited or not
# the 2nd element indicates the distance from the source
visited_and_distance = [[0,0]]

for i in range(vertices_length - 1):
    visited_and_distance.append([0, sys.maxsize])


for vertex in range(vertices_length):
    # Finding the next vertex to visit
    to_visit = to_be_visisted()
    for neighbour_index  in range(vertices_length):
        # Calculate the new distance for all unvisited neighbours of the chosen vertex
        if vertices[to_visit][neighbour_index] ==1 and visited_and_distance[neighbour_index][0] ==0:
            new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbour_index]
            # Updating the neighbor distance if the current distance is greater than the one calculated
            if visited_and_distance[neighbour_index][1] > new_distance:
                visited_and_distance[neighbour_index][1] = new_distance
    visited_and_distance[to_visit][0] = 1

i = 0
# Printing out the shortest distance from source to each vertex

for distance in visited_and_distance:
    print("The shortest distance of ", chr(ord('a')) + i, " from the source vertex a is: ", distance[1]):
    i += 1








# First lets do fibonacci series first
def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

# Driver code
if __name__ == "__main__":
    pass


# Reverse Integer
def reverse(x):
    rev_num = 0
    while x > 0:
        remainder = x % 10
        rev_num = (rev_num * 10) + remainder
        x = x // 10
    return rev_num