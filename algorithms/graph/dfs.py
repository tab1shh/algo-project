# graph is dict where keys represent nodes, and values are sets or lists of adjacent nodes
def dfs(graph, start, visited=None):
    if visited is None:
        # initialize as empty set and will be used to keep track of allnodes that have been visited
        visited = set()
    visited.add(start)  # adds start node to visited list
    # iterates all node adjacent to the 'start' node. adjacency is retrieved from 'graph[start]' and then the nodes that have already been visited are subtracted with '- visited'
    # makes sure only unvisited nodes are considered for this step
    for next in graph[start] - visited:
        # recursivley calls itself with the new 'start' node as 'next'
        dfs(graph, next, visited)
    return visited


def main():
    # Define the graph
    graph = {
        "A": {"B", "C"},
        "B": {"A", "D", "E"},
        "C": {"A", "F"},
        "D": {"B"},
        "E": {"B", "F"},
        "F": {"C", "E"},
    }

    # Perform DFS starting from node 'A'
    visited_nodes = dfs(graph, "A")

    # Print the result
    print("Visited nodes:", visited_nodes)


if __name__ == "__main__":
    main()
