def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recursivley call and continue to do until each subarray has only one element
        merge_sort(left)
        merge_sort(right)

        # 'i' is the index for going left of the subarray
        # 'j' is the index for going right of the subarray
        # 'k' is the index for placing the merged elements back into the original array 'arr'
        i = j = k = 0

        # continues as long as left and right subarrays have unmerged elements
        while i < len(left) and j < len(right):
            # if current element in left is smaller than right, smaller element is placed into arr[k], 'i' is then incremeneted to move to the next element in the left subarray
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1  # after placing the smaller element into arr[k], k is incremented to mvoe to the next position in the array

        # if there any remaining elements in the left subarray, they are copied into arr, and this runs until all elements in left have been merged
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
