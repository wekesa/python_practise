
'''
- Graph is a data structure that consists of vertices and edges
- Can be implemented with an
    - Adjacency list
        - For each vertex its adjacent vertices are stored
    - Adjacency matrix
        - The row and the column indices represent the vertices: matrix[i][j]
        -
-
'''

import re
# Add a vertex to the dictionary
def add_vertex(v):
    """
    :param v:
    :return:
    """
    global graph
    global vertices_no
    if v in graph:
        print("Vertex " + v + " Alredy exists")
    else:
        vertices_no = vertices_no + 1
        graph[v] = []


# Add an edge between v1 and v2 with an edge weight  e
def add_edge(v1, v2, e):
    global graph
    # Check if v1 is in the graph
    if v1 not in graph:
        print("Vertex " + v1 + " does not exists")
    if v2 not in graph:
        print("Vertex " + v2 + " Does not exists")
    else:
        temp = [v2, e]
        graph[v1].append(temp)

def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, "->", edges[0], "edge weight: ", edges[1])



def find_longest_sequence_non_repeating_strings(S):
    n = len(str)

    # Result
    res = 0

    for i in range(n):

        # Note : Default values in
        # visited are false
        visited = [0] * 256

        for j in range(i, n):

            # If current character is visited
            # Break the loop
            if (visited[ord(str[j])] == True):
                break

            # Else update the result if
            # this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True

        # Remove the first character of previous
        # window
        visited[ord(str[i])] = False

    return res


def check_if_pattern_matches(S):
    valid_pattern = r'[\d+]'
    if re.match(valid_pattern, S):
        return False
    else:
        return True


def remove_digits(sentence):
    """
    @desc Get a string which is a sentence
    @params s
    :param sentence:
    :return:
    """
    return ''.join(i for i in sentence if not i.isdigit())