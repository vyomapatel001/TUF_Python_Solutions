def insertionSort(arr):
    """
    Perform insertion sort on the array to sort it in ascending order.

    :param arr: List of elements to be sorted.
    """
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



# Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
# Time Complexity: O(n^2) where n is the number of elements in the array.
# Space Complexity: O(1) since it uses a constant amount of space.
# Insertion Sort is a stable sort, meaning that it preserves the relative order of equal elements.

if __name__ == "__main__":
    # Example usage
    arr = [12, 11, 13, 5, 6]
    print("Unsorted array is:")
    print(arr)
    insertionSort(arr)
    print("Sorted array is:")
    print(arr)