import sys


def dijkstra(graph, start):
    # initialize the visited dictionary with the start node having distance 0
    visited = {start: 0}
    # initialize the path dictionary to store the shortest path tree
    path = {}

    # initialize a set of all nodes in the graph
    nodes = set(graph.keys())

    while nodes:
        # find the node with the smallest known distance
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        # if no minimum node is found, exit the loop
        if min_node is None:
            break

        # remove the min_node from the set of nodes to process
        nodes.remove(min_node)
        # get the current shortest distance to the min_node
        current_weight = visited[min_node]

        # update distances to adjacent nodes
        for edge in graph[min_node]:
            weight = current_weight + graph[min_node][edge]
            # update the shortest distance and path if a shorter path is found
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    # return the shortest distances and the path tree
    return visited, path
