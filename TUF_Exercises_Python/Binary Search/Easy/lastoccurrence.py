def lastoccurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1  # Initialize result to -1 to handle case where target is not found
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            low = mid + 1  # Move to the right side to find the last occurrence
        elif arr[mid] < target:
            low = mid + 1  # Move to the right side
        else:
            high = mid - 1
    return result  # Return the index of the last occurrence or -1 if not found

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = lastoccurrence(arr, target)
    
    if result != -1:
        print(f"The last occurrence of {target} is at index {result}.")
    else:
        print(f"{target} is not present in the array.")
# Output: The last occurrence of 2 is at index 2.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Brute Force Approach
def lastoccurrenceBruteForce(arr, target):
    """
    Find the last occurrence of a target in a sorted array using brute force.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find the last occurrence for.
    :return: int - The index of the last occurrence of the target or -1 if not found.
    """
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1
# Example usage for brute force approach
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = lastoccurrenceBruteForce(arr, target)
    
    if result != -1:
        print(f"The last occurrence of {target} using brute force is at index {result}.")
    else:
        print(f"{target} is not present in the array.")
# Output: The last occurrence of 2 using brute force is at index 2.
# Time Complexity: O(n)
# Space Complexity: O(1)
# The brute force approach is less efficient than the binary search approach, especially for large arrays.