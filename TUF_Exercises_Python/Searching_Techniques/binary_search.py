
def binary_search(arr, target, low, high):
    """
    Perform a binary search on the sorted array to find the target element.

    :param arr: Sorted list of elements to search in.
    :param target: Element to search for.
    :param low: Starting index of the search range.
    :param high: Ending index of the search range.
    :return: Index of the target element if found, otherwise -1.
    """
    if low <= high:
        # Calculate the middle index    
        mid = (high + low) // 2  # Find the middle index

        # If the element is present at the middle itself
        if arr[mid] == target:
            return mid
        # If the element is smaller than mid, then it can only be present in the left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        # If the element is larger than mid, then it can only be present in the right subarray
        else:
            return binary_search(arr, target, mid + 1, high)
        
    
    # Element is not present in array
    return -1
# Binary Search is a more efficient search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.
# Time Complexity: O(log n) where n is the number of elements in the array.
# Space Complexity: O(1) for the iterative version, O(log n) for the recursive version due to call stack space.

if __name__ == "__main__":
    # Example usage
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(sorted(arr), target, 0, len(arr) - 1)
    if result != -1:
        print(f"Binary Search: Element found at index {result}")
    else:
        print("Binary Search: Element not found")