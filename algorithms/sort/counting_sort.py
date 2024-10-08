def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1  # used to create a count array
    # a list 'count' with size 'm' initialized with all elements 0, this will store the freq of each value in arr
    count = [0] * m

    for a in arr:
        # increments the index in 'count', tracking how many times 'a' appears in 'arr'
        count[a] += 1

    i = 0  # will be used to place elements back into original 'arr' sorted
    for a in range(m):
        # runs count[a] times corresponding to the number of occurences of the value 'a' in 'arr'
        # for each occurence the value 'a' is palced into the original 'arr' at the current index 'i'
        for c in range(count[a]):
            arr[i] = a  # 'a' is places at index 'i' in the original 'arr'
            i += 1  # move to the next position in 'arr'
    return arr


def main():
    # Test cases
    arr1 = [4, 10, 3, 5, 1]
    arr2 = [12, 11, 13, 5, 6, 7]

    print("Original array 1:", arr1)
    sorted_arr1 = counting_sort(arr1)
    print("Sorted array 1:", sorted_arr1)

    print("Original array 2:", arr2)
    sorted_arr2 = counting_sort(arr2)
    print("Sorted array 2:", sorted_arr2)


if __name__ == "__main__":
    main()
