def partition(arr, low, high):
    """
    This function takes the last element as pivot, places the pivot element at its correct position in sorted array,
    and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot.

    :param arr: List of elements to be sorted.
    :param low: Starting index of the subarray.
    :param high: Ending index of the subarray.
    :return: The index of the pivot element after partitioning.
    """
    i = low - 1  # Index of smaller element
    pivot = arr[high]  # Pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i + 1
    return i + 1
def quickSort(arr, low, high):
    """
    The main function that implements QuickSort.
    arr[] is the array to be sorted,
    low is the starting index and high is the ending index.

    :param arr: List of elements to be sorted.
    :param low: Starting index of the subarray.
    :param high: Ending index of the subarray.
    """
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Recursively sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

if __name__ == "__main__":
    # Example usage
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    quickSort(arr, 0, n - 1)

    print("Sorted array is")
    for i in range(n):
        print(arr[i], end=" ")
    print()

# QuickSort is an efficient sorting algorithm that uses a divide-and-conquer approach to sort elements.
# Time Complexity: O(n log n) on average, O(n^2) in the worst case.
# Space Complexity: O(log n) due to the recursive stack space.
# QuickSort is not a stable sort, meaning that it does not preserve the relative order of equal elements.