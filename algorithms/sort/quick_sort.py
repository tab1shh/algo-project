# low is the starting portion of the array, high is the ending
def partition(arr, low, high):
    pivot = arr[high]  # pivot element chosen is the high index of the array
    i = low - 1  # used to track where the next smaller element should be placed
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # places pivot element in correct spot by swapping, now elements to the left of the pivot are smaller or equal and elements to the right are larger
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    # if high is not provided, it is set to the last index of the array
    if high is None:
        high = len(arr) - 1
    # ensures the function only continues if the low index is less than the high index, meaning there are still elements to be sorted
    if low < high:
        # returns index 'pi' whihc is the correct position of the pivot in the sorted array
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)  # recursivley called on the left subarray
        quick_sort(arr, pi + 1, high)  # recursivley called on the right subarray
    return arr


def main():
    # Test cases
    arr1 = [4, 10, 3, 5, 1]
    arr2 = [12, 11, 13, 5, 6, 7]

    print("Original array 1:", arr1)
    sorted_arr1 = quick_sort(arr1)
    print("Sorted array 1:", sorted_arr1)

    print("Original array 2:", arr2)
    sorted_arr2 = quick_sort(arr2)
    print("Sorted array 2:", sorted_arr2)


if __name__ == "__main__":
    main()
