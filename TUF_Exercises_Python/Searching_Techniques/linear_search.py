
def linear_search(arr, target):
    """
    Perform a linear search on the array to find the target element.

    :param arr: List of elements to search in.
    :param target: Element to search for.
    :return: Index of the target element if found, otherwise -1.
    """
    for num in range(len(arr)):
        if arr[num] == target:
            return num
    return -1  # Return -1 if the target is not found in the array
# Linear Search is a simple search algorithm that checks each element in the list sequentially until the target element is found or the end of the list is reached.
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) since it uses a constant amount of space.

if __name__ == "__main__":
    # Example usage
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = linear_search(arr, target)
    if result != -1:
        print(f"Linear Search: Element found at index {result}")
    else:
        print("Linear Search: Element not found")