class Graph:
    def __init__(self, vertices):
        # initialize the number of vertices and the list to hold edges
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        # add an edge to the graph with vertices u, v and weight w
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # initialize distances from src to all other nodes as infinity
        dist = [float("Inf")] * self.V
        # distance from src to itself is always 0
        dist[src] = 0

        # relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                # check if the distance to v can be shortened by taking the edge u-v
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # check for negative weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return "Graph contains negative weight cycle"

        return dist


def main():
    # Create a graph with 5 vertices
    g = Graph(5)

    # Add edges with weights
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 3, -3)

    # Run Bellman-Ford algorithm from vertex 0
    distances = g.bellman_ford(0)

    # Print the results
    if isinstance(distances, str):
        print(distances)
    else:
        print("Shortest distances from vertex 0:")
        for i, dist in enumerate(distances):
            print(f"Distance to vertex {i}: {dist}")


if __name__ == "__main__":
    main()
