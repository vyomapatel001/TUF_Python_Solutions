def bubble_sort(arr):
    """
    Perform bubble sort on the array to sort it in ascending order.

    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Flag to check if a swap occurred
        
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
    
    # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break  # If no swaps occurred, the array is sorted

if __name__ == "__main__":
    # Example usage
    arr = [39, 12, 18, 85, 72, 10, 2, 18]
    print("Unsorted list is:")
    print(arr)

    bubble_sort(arr)

    print("Sorted list is:")
    print(arr)

# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# Time Complexity: O(n^2) where n is the number of elements in the array.
# Space Complexity: O(1) since it uses a constant amount of space.