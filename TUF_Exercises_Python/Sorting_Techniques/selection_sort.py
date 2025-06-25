def selectionSort(arr, size):
    """
    Perform selection sort on the array to sort it in ascending order.

    :param arr: List of elements to be sorted.
    :param size: Size of the array.
    """
    for i in range(size):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    # Example usage
    arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
    print("Unsorted array is:")
    print(arr)

    selectionSort(arr, size=len(arr))

    print("Sorted array is:")
    print(arr)

# Selection Sort is a simple sorting algorithm that divides the input list into two parts: a sorted and an unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part.
# Time Complexity: O(n^2) where n is the number of elements in the array.
# Space Complexity: O(1) since it uses a constant amount of space.
# Selection Sort is not a stable sort, meaning that it does not preserve the relative order of equal elements.