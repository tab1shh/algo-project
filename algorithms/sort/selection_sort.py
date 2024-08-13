def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        # starts from element right after i and goes until last index
        for j in range(i + 1, len(arr)):
            # checks if the current element is smaller than the current min, and if its true update min_idx to be j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def main():
    # Test cases
    arr1 = [4, 10, 3, 5, 1]
    arr2 = [12, 11, 13, 5, 6, 7]

    print("Original array 1:", arr1)
    sorted_arr1 = selection_sort(arr1)
    print("Sorted array 1:", sorted_arr1)

    print("Original array 2:", arr2)
    sorted_arr2 = selection_sort(arr2)
    print("Sorted array 2:", sorted_arr2)


if __name__ == "__main__":
    main()
