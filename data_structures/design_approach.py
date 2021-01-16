"""
Design Questions
 - Use cases
 - Out of scope
 - Constraints 559155 5591
 - High Level
 - Use Dijkstra's
 - Layers
     - Data layer (No-SQL vs SQL)
     - Micro - services
     - Client side
     - CI/CD
"""

"""
 - Given a list of packages that need to be built and the dependencies for each package
 determine a valid order in which to build the package
 - e.g
 0:
 1: 0
 2: 0
 3: 1, 2
 4: 3
 
 Output: 0, 1, 2, 3, 4
 Time complexity O(V+E)
 Topological sort
 Test cases
"""


def package_dependencies(dependencies):
    result = []
    visiting = set([])
    visited = set([])

    def dfs(node):
        if node in visited:
            return
        visiting.add(node)
        for neighbour in dependencies[node]:
            if neighbour in visiting:
                raise Exception("Cycle in dependency graph")
            if neighbour not in visited:
                dfs(neighbour)
        visiting.remove(node)
        visited.add(node)
        result.append(node)

    for node in dependencies.keys():
        dfs(node)
    return result


mapping = {
    0: [],
    1: [0],
    2: [0],
    3: [1, 2],
    4: [3]
}

print(package_dependencies(mapping))
