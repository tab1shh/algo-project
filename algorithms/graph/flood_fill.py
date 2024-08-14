def flood_fill(screen, x, y, prev_color, new_color):
    # Check if the current position is out of bounds
    if x < 0 or x >= len(screen) or y < 0 or y >= len(screen[0]):
        return

    # Check if the current pixel color is not the target color to replace
    if screen[x][y] != prev_color:
        return

    # Replace the color of the current pixel
    screen[x][y] = new_color

    # Recursively call flood_fill to adjacent pixels (up, down, left, right)
    flood_fill(screen, x + 1, y, prev_color, new_color)  # Move down
    flood_fill(screen, x - 1, y, prev_color, new_color)  # Move up
    flood_fill(screen, x, y + 1, prev_color, new_color)  # Move right
    flood_fill(screen, x, y - 1, prev_color, new_color)  # Move left


def print_screen(screen):
    for row in screen:
        print(" ".join(map(str, row)))
    print()


def main():
    # Define a 2D screen (grid) with colors
    screen = [[1, 1, 1, 2, 2], [1, 2, 2, 2, 2], [1, 2, 1, 1, 1], [1, 1, 1, 1, 1]]

    # Print the original screen
    print("Original screen:")
    print_screen(screen)

    # Perform flood fill operation
    flood_fill(screen, 1, 1, 2, 3)

    # Print the screen after flood fill
    print("Screen after flood fill:")
    print_screen(screen)


if __name__ == "__main__":
    main()
