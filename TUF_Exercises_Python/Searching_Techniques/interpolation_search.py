def interpolation_search(arr, target):
    """
    Perform an interpolation search on the sorted array to find the target element. 
    :param arr: Sorted list of elements to search in.
    :param target: Element to search for.
    :return: Index of the target element if found, otherwise -1.
    """

    low = 0
    high = len(arr) - 1

    while low <=high and target >= arr[low] and target <= arr[high]:
        # Calculate the position using interpolation formula
        pos = low + (high-low) * (target - arr[low]) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1  # Return -1 if the target is not found in the array
# Interpolation Search is an improved version of binary search that works on sorted arrays by estimating the position of the target element based on its value.
# Time Complexity: O(log log n) for uniformly distributed data, O(n) in the worst case.
# Space Complexity: O(1) since it uses a constant amount of space.

if __name__ == "__main__":
    # Example usage
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = interpolation_search(sorted(arr), target)
    if result != -1:
        print(f"Interpolation Search: Element found at index {result}")
    else:
        print("Interpolation Search: Element not found")