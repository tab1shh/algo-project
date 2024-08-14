def boyer_moore_majority_vote(arr):
    """
    Find the majority element in the array using the Boyer-Moore Voting Algorithm.
    If no majority element exists, return None.
    """
    count = 0  # Initialize the count of the current candidate
    candidate = None  # Initialize the candidate for majority element

    # Iterate through each element in the array
    for num in arr:
        if count == 0:
            candidate = num  # Update the candidate if count is zero
        # Increment or decrement the count based on whether the current element matches the candidate
        count += 1 if num == candidate else -1

    # Verify if the candidate is actually the majority element
    return candidate if arr.count(candidate) > len(arr) // 2 else None


def main():
    arr1 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    arr2 = [3, 3, 4, 2, 4, 4, 2, 4]

    # Find the majority element in both arrays
    result1 = boyer_moore_majority_vote(arr1)
    result2 = boyer_moore_majority_vote(arr2)

    # Print the results
    print("Majority element in arr1:", result1)  # Should print 4
    print("Majority element in arr2:", result2)  # Should print None


if __name__ == "__main__":
    main()
