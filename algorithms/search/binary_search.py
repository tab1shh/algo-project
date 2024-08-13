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
