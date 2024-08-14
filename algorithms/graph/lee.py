from collections import deque


def is_valid_move(matrix, visited, row, col):
    # Check if the move is within the bounds of the matrix and if the cell is valid
    return (
        0 <= row < len(matrix)
        and 0 <= col < len(matrix[0])
        and matrix[row][col] == 1
        and not visited[row][col]
    )


def lee(matrix, src, dest):
    # Define possible movements: up, left, right, down
    rows = [-1, 0, 0, 1]
    cols = [0, -1, 1, 0]

    # Initialize the visited matrix and the queue for BFS
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    queue = deque([(src, 0)])  # Queue holds tuples of (position, distance)

    # Mark the source cell as visited
    visited[src[0]][src[1]] = True

    # Perform BFS
    while queue:
        current, dist = queue.popleft()
        row, col = current

        # Check if we have reached the destination
        if (row, col) == dest:
            return dist

        # Explore all 4 possible directions (up, down, left, right)
        for i in range(4):
            new_row, new_col = row + rows[i], col + cols[i]

            # Check if the new move is valid and not visited
            if is_valid_move(matrix, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), dist + 1))

    # Return -1 if destination is not reachable
    return -1


def main():
    # Define a matrix where 1 represents open cells and 0 represents blocked cells
    matrix = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]

    # Define source and destination coordinates
    src = (0, 0)
    dest = (4, 4)

    # Run Lee's algorithm
    result = lee(matrix, src, dest)

    # Print the result
    print("Shortest path distance:", result)


if __name__ == "__main__":
    main()
