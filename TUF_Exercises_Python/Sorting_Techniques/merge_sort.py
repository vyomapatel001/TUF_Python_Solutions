def mergeSort(arr, l, r):
    """
    Perform merge sort on the array to sort it in ascending order.

    :param arr: List of elements to be sorted.
    :param l: Left index of the subarray.
    :param r: Right index of the subarray.
    """
    if l < r:
        # Find the middle point
        m = (l + r) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Merge the sorted halves
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    """
    Merge two subarrays of arr[].

    :param arr: List of elements to be merged.
    :param l: Left index of the first subarray.
    :param m: Right index of the first subarray (middle).
    :param r: Right index of the second subarray.
    """
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # Example usage
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")

    mergeSort(arr, 0, n - 1)

    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")
    print()


# Merge Sort is a divide and conquer algorithm that divides the array into halves, sorts each half, and then merges them back together.
# Time Complexity: O(n log n) where n is the number of elements in the array.
# Space Complexity: O(n) due to the temporary arrays used for merging.
# Merge Sort is a stable sort, meaning that it preserves the relative order of equal elements.
# Merge Sort is particularly useful for large datasets and is often used in external sorting algorithms.