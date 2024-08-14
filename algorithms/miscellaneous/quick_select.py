def partition(arr, low, high):
    """
    Partition the array into elements less than the pivot and elements greater than the pivot.
    """
    pivot = arr[high]  # Choose the pivot element (last element in the current range)
    i = low  # Initialize the partition index

    # Iterate over the array from 'low' to 'high - 1'
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than the pivot
            arr[i], arr[j] = (
                arr[j],
                arr[i],
            )  # Swap elements to ensure smaller elements are on the left side
            i += 1  # Move the partition index to the right

    # Place the pivot element in its correct position
    arr[i], arr[high] = arr[high], arr[i]
    return i  # Return the partition index


def quick_select(arr, k, low=0, high=None):
    """
    Find the k-th smallest element in an unordered list using Quickselect algorithm.
    """
    if high is None:
        high = len(arr) - 1  # Set high to the last index if not provided

    if low == high:
        return arr[low]  # If the list contains only one element, return it

    # Partition the array and get the index of the pivot element
    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[k]  # If the pivot index is the k-th index, return the pivot element
    elif k < pivot_index:
        return quick_select(arr, k, low, pivot_index - 1)  # Search in the left subarray
    else:
        return quick_select(
            arr, k, pivot_index + 1, high
        )  # Search in the right subarray


def main():
    arr = [10, 5, 2, 7, 6, 1]
    k = 3  # Find the 3rd smallest element (0-based index)

    # Find the k-th smallest element
    result = quick_select(arr, k)

    # Print the result
    print("The", k, "th smallest element is:", result)


if __name__ == "__main__":
    main()
