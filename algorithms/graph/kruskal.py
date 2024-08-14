class Graph:
    def __init__(self, vertices):
        # number of vertices and the list to hold edges
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        # add an edge to the graph with a weight
        self.graph.append([u, v, w])

    def find(self, parent, i):
        # find the root of the set in which element i belongs
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        # perform union of two subsets x and y
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        # main func to construct MST using Kruskals algo
        result = []  # store the resultant MST
        i, e = 0, 0  # initialize index var for edges and results

        # sort all the edhes in non dereasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # initialize parent and rank arrays
        parent = []
        rank = []

        # create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # number of edhes to be taken is equal to V-1
        while e < self.V - 1:
            # pick the smallest edge, check if it forms a cycle with the spanning tree formed so far
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including this edge does not cause a cycle, include it in the result and union the two subsets
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result  # return constructed MST


def main():
    # Create a graph with 4 vertices
    g = Graph(4)

    # Add edges with weights
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    # Find the MST using Kruskal's algorithm
    mst = g.kruskal()

    # Print the edges in the MST
    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")


if __name__ == "__main__":
    main()
