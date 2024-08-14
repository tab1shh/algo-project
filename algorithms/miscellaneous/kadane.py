def kadane(arr):
    # Initialize `max_current` and `max_global` with the first element of the array
    max_current = max_global = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update `max_current` to be the maximum of the current element or the sum of `max_current` and the current element
        max_current = max(arr[i], max_current + arr[i])

        # Update `max_global` if `max_current` is greater than `max_global`
        if max_current > max_global:
            max_global = max_current

    # Return the maximum sum of a contiguous subarray
    return max_global


def main():
    # Define an array of integers
    arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]

    # Run Kadane's Algorithm
    result = kadane(arr)

    # Print the result
    print("Maximum sum of a contiguous subarray:", result)


if __name__ == "__main__":
    main()
