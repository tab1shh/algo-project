def topological_sort_util(v, visited, stack, graph):
    # Mark the current node as visited
    visited[v] = True
    # Recursively visit all the adjacent vertices of the current vertex
    for i in graph[v]:
        if not visited[i]:
            topological_sort_util(i, visited, stack, graph)
    # Push the current vertex to the stack to represent it in the topological order
    stack.insert(0, v)


def topological_sort(graph):
    # Initialize a list to keep track of visited vertices
    visited = [False] * len(graph)
    # Initialize a stack to store the topological sort order
    stack = []

    # Perform topological sort for each vertex
    for i in range(len(graph)):
        if not visited[i]:
            topological_sort_util(i, visited, stack, graph)

    return stack


def main():
    # Define a graph as an adjacency list
    # The graph is represented as a list of lists where each list contains the adjacent vertices
    graph = [
        [1, 2],  # Vertex 0 is connected to vertices 1 and 2
        [3],  # Vertex 1 is connected to vertex 3
        [3],  # Vertex 2 is connected to vertex 3
        [],  # Vertex 3 has no outgoing edges
    ]

    # Run topological sort on the graph
    order = topological_sort(graph)

    # Print the topological order
    print("Topological order:", order)


if __name__ == "__main__":
    main()
