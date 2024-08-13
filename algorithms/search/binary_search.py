def binary_search(arr, target):
    left = 0  # starting index of list
    right = len(arr) - 1  # ending index of list
    while left <= right:  #
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif (
            arr[mid] < target
        ):  # checks if 'mid' is less than target meaning it must be on the right half of current range
            left = (
                mid + 1
            )  # if target is on right half then it update the left index, narrowing the search to the right half of the array
        else:  # target must be on the left half of current range
            right = mid + 1  # updates right to narrow search to left half of array
    return -1


def main():
    # Test cases
    arr1 = [10, 20, 30, 40, 50]
    arr2 = [5, 15, 25, 35, 45]
    arr3 = [1, 2, 3, 4, 5]

    # Test 1: Target is present in the middle
    target1 = 30
    result1 = binary_search(arr1, target1)
    print(f"Test 1 - Searching for {target1} in {arr1}: Index {result1}")

    # Test 2: Target is present at the end
    target2 = 45
    result2 = binary_search(arr2, target2)
    print(f"Test 2 - Searching for {target2} in {arr2}: Index {result2}")

    # Test 3: Target is not present
    target3 = 100
    result3 = binary_search(arr1, target3)
    print(f"Test 3 - Searching for {target3} in {arr1}: Index {result3}")

    # Test 4: Target is present at the beginning
    target4 = 1
    result4 = binary_search(arr3, target4)
    print(f"Test 4 - Searching for {target4} in {arr3}: Index {result4}")

    # Test 5: Empty array
    target5 = 10
    result5 = binary_search([], target5)
    print(f"Test 5 - Searching for {target5} in an empty array: Index {result5}")


if __name__ == "__main__":
    main()
