def heapfiy(arr, n, i):
    largest = i  # largest is index of the current node
    # calculate left and right children of node at index i
    left = 2 * i + 1
    right = 2 * i + 2
    # checks if left child exists and if its greater than the current node value, if so, update left to be the largest
    if left < n and arr[i] < arr[left]:
        largest = left
    # checks if right child exists and if its greater than the current node value, if so, update right to be the largest
    if right < n and arr[largest] < arr[right]:
        largest = right
    # if largest has been updated (not original index at i) swap the values of arr[i] and largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursivley call heapify() to ensure the subtree rooted at largest satisfies the max heap property
        heapfiy(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # n // 2 calculates the index of the first no-leaf node, subtracting 1 adjusts the starting index to be the last non-leaf node
    # loop run while 'i' is >= -1
    # 'i' decreases by 1 each iteration
    for i in range(n // 2 - 1, -1, -1):
        heapfiy(arr, n, i)  # called to restore heap property

    # starts from last index of array
    # runs while 'i' >= 0
    # 'i' decreases by 1 each iteration
    for i in range(n - 1, 0, -1):
        # move the root of heap (max value) to the end of the array at index i, basically swapping first and last
        arr[i], arr[0] = arr[0], arr[i]
        heapfiy(arr, i, 0)  # called to restore heap property
    return arr


def main():
    # Test cases
    arr1 = [4, 10, 3, 5, 1]
    arr2 = [12, 11, 13, 5, 6, 7]

    print("Original array 1:", arr1)
    sorted_arr1 = heap_sort(arr1)
    print("Sorted array 1:", sorted_arr1)

    print("Original array 2:", arr2)
    sorted_arr2 = heap_sort(arr2)
    print("Sorted array 2:", sorted_arr2)


if __name__ == "__main__":
    main()
