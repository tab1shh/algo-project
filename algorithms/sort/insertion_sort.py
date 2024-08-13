def insertion_sort(arr):
    for i in range(1, len(arr)):
        # stores the value of current element into key, this is the element that needs to be inserted into the sorted portion of the array
        key = arr[i]
        # initializes j to be in the index just before i, used to compare key with elements in the sorted portion of the array
        j = i - 1
        while j >= 0 and key < arr[j]:
            # shift elements at index j to the right, making space for the key to be inserted into correct position
            arr[j + 1] = arr[j]
            j -= 1  # decreases j by 1 to continue comparing key with the next elelment to the left in the sorted portion
        arr[j + 1] = key
    return arr


def main():
    # Test cases
    arr1 = [5, 2, 9, 1, 5, 6]
    arr2 = [3, 1, 4, 1, 5, 9, 2, 6]
    arr3 = [10, 7, 8, 9, 1, 2]

    # Test 1
    print("Original array:", arr1)
    sorted_arr1 = insertion_sort(arr1)
    print("Sorted array:", sorted_arr1)

    # Test 2
    print("Original array:", arr2)
    sorted_arr2 = insertion_sort(arr2)
    print("Sorted array:", sorted_arr2)

    # Test 3
    print("Original array:", arr3)
    sorted_arr3 = insertion_sort(arr3)
    print("Sorted array:", sorted_arr3)


if __name__ == "__main__":
    main()
