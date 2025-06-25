def lowerBound(arr, target):
    """
    Find the lower bound of a target in a sorted array.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find the lower bound for.
    :return: int - The index of the first occurrence of the target or the index where it can be inserted.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        # If mid element is less than target, move left pointer
        # Otherwise, move right pointer to find the lower bound
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = lowerBound(arr, target)
    
    print(f"The lower bound of {target} in the array is at index {result}.")
    # Output: The lower bound of 2 in the array is at index 1.

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Brute Force Approach
def lowerBoundBruteForce(arr, target):
    """
    Find the lower bound of a target in a sorted array using brute force.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find the lower bound for.
    :return: int - The index of the first occurrence of the target or the index where it can be inserted.
    """
    for i in range(len(arr)):
        if arr[i] >= target:
            return i
    return len(arr)
# Example usage for brute force approach
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = lowerBoundBruteForce(arr, target)
    
    print(f"The lower bound of {target} in the array using brute force is at index {result}.")
    # Output: The lower bound of 2 in the array using brute force is at index 1.
# Time Complexity: O(n)
# Space Complexity: O(1)
# The brute force approach is less efficient than the binary search approach, especially for large arrays.