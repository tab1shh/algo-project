from collections import deque


def bfs(graph, start):
    # empty set to keep track of visited nodes
    visited = set()
    # a queue with the starting node
    queue = deque([start])
    # cont processing nodes until queue is empty
    while queue:
        # remove and return the leftmost node from the queue
        vertex = queue.popleft()
        # check if node has not been visited
        if vertex not in visited:
            # mark as visited
            visited.add(vertex)
            # add all unvisited nodes to the queue
            queue.extend(graph[vertex] - visited)
    return visited
