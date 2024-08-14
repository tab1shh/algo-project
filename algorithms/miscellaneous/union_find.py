class UnionFind:
    def __init__(self, size):
        """
        Initializes a Union-Find (Disjoint Set) data structure.

        Parameters:
        size (int): The number of elements in the Union-Find structure.
        """
        self.parent = list(range(size))  # Each element is its own parent initially
        self.rank = [0] * size  # Ranks are initialized to 0 for all elements

    def find(self, p):
        """
        Finds the root of the element p with path compression.

        Parameters:
        p (int): The element to find the root of.

        Returns:
        int: The root of the element p.
        """
        if self.parent[p] != p:  # If p is not the root
            self.parent[p] = self.find(
                self.parent[p]
            )  # Path compression: make p directly point to its root
        return self.parent[p]  # Return the root of p

    def union(self, p, q):
        """
        Unites the sets containing elements p and q.

        Parameters:
        p (int): The first element.
        q (int): The second element.
        """
        rootP = self.find(p)  # Find the root of p
        rootQ = self.find(q)  # Find the root of q

        if rootP != rootQ:  # Only unite if they are in different sets
            # Attach the smaller rank tree under the root of the larger rank tree
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP  # Root of q points to root of p
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ  # Root of p points to root of q
            else:
                # If ranks are equal, make one root point to the other and increase the rank
                self.parent[rootQ] = rootP  # Root of q points to root of p
                self.rank[rootP] += 1  # Increase the rank of the new root
