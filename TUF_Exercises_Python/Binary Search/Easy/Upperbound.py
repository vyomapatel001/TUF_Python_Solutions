def upperBound(arr, target):
    """
    Find the upper bound of a target in a sorted array.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find the upper bound for.
    :return: int - The index of the first element greater than the target, or len(arr) if no such element exists.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
            
    return left

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = upperBound(arr, target)
    
    print(f"The upper bound of {target} in the array is at index {result}.")
    # Output: The upper bound of 2 in the array is at index 3.

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Brute Force Approach
def upperBoundBruteForce(arr, target):
    """
    Find the upper bound of a target in a sorted array using brute force.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find the upper bound for.
    :return: int - The index of the first element greater than the target, or len(arr) if no such element exists.
    """
    for i in range(len(arr)):
        if arr[i] > target:
            return i
    return len(arr)

# Example usage for brute force approach
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = upperBoundBruteForce(arr, target)
    
    print(f"The upper bound of {target} in the array using brute force is at index {result}.")
    # Output: The upper bound of 2 in the array using brute force is at index 3.