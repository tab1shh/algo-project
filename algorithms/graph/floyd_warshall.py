def floyd_warshall(graph):
    # Initialize the distance matrix `dist` with the given graph
    # Create a deep copy of the graph to avoid modifying the original
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))

    # Iterate over all vertices to update the distance matrix
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # Update the distance between i and j by considering vertex k as an intermediate vertex
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    # Define the graph as an adjacency matrix
    # Use float("inf") to represent no direct edge between nodes
    graph = [
        [0, 3, float("inf"), float("inf"), float("inf")],
        [2, 0, float("inf"), 1, float("inf")],
        [float("inf"), 7, 0, float("inf"), 2],
        [float("inf"), float("inf"), 6, 0, float("inf")],
        [float("inf"), float("inf"), float("inf"), 4, 0],
    ]

    # Run Floyd-Warshall algorithm
    distances = floyd_warshall(graph)

    # Print the results
    print("Shortest distances between every pair of vertices:")
    for i in range(len(distances)):
        print(f"From vertex {i}: {distances[i]}")


if __name__ == "__main__":
    main()
