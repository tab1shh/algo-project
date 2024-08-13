def linear_search(arr, target):
    # enumerate is a function thast return both the index and element at taht index in the list 'arr'
    # as the loop goes through the list, 'index' will be the position of the current element and 'element' will be the value of that element
    for index, element in enumerate(arr):
        if (
            element == target
        ):  # checks if element has been found, and returns the index of the element
            return index
    return -1  # returns if target is not found


def main():
    # Test cases
    arr1 = [10, 20, 30, 40, 50]
    arr2 = [5, 15, 25, 35, 45]
    arr3 = [1, 2, 3, 4, 5]

    # Test 1: Target is present in the middle
    target1 = 30
    result1 = linear_search(arr1, target1)
    print(f"Test 1 - Searching for {target1} in {arr1}: Index {result1}")

    # Test 2: Target is present at the end
    target2 = 45
    result2 = linear_search(arr2, target2)
    print(f"Test 2 - Searching for {target2} in {arr2}: Index {result2}")

    # Test 3: Target is not present
    target3 = 100
    result3 = linear_search(arr1, target3)
    print(f"Test 3 - Searching for {target3} in {arr1}: Index {result3}")

    # Test 4: Target is present at the beginning
    target4 = 1
    result4 = linear_search(arr3, target4)
    print(f"Test 4 - Searching for {target4} in {arr3}: Index {result4}")

    # Test 5: Empty array
    target5 = 10
    result5 = linear_search([], target5)
    print(f"Test 5 - Searching for {target5} in an empty array: Index {result5}")


if __name__ == "__main__":
    main()
