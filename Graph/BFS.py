from collections import deque

graph = {1: set([3,4]),
         2: set([3,4,5]),
         3: set([1,5]),
         4: set([1]),
         5: set([2,6]),
         6: set([3,5])
         }
rootNode = 1


def BFS(graph,rootNode):
    queue = deque([rootNode])
    visited = []

    while queue:
        n = queue.popleft()
        visited.append(n)

        for i in graph[n]:
            if i not in visited:
                queue.append(i)
    return visited


print(BFS(graph,rootNode))
