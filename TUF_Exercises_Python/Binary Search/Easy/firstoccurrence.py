def firstoccurrence(arr, target):
    """
    Find the first occurrence of a target value in a sorted array.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find.
    :return: int - The index of the first occurrence of the target, or -1 if not found.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = firstoccurrence(arr, target)
    
    if result != -1:
        print(f"The first occurrence of {target} is at index {result}.")
    else:
        print(f"{target} is not present in the array.")
# Output: The first occurrence of 2 is at index 1.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Brute Force Approach
def firstoccurrenceBruteForce(arr, target):
    """
    Find the first occurrence of a target value in a sorted array using brute force.
    
    :param arr: List[int] - A sorted list of integers.
    :param target: int - The target value to find.
    :return: int - The index of the first occurrence of the target, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Example usage for brute force approach
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5]
    target = 2
    result = firstoccurrenceBruteForce(arr, target)
    
    if result != -1:
        print(f"The first occurrence of {target} using brute force is at index {result}.")
    else:
        print(f"{target} is not present in the array.")
# Output: The first occurrence of 2 using brute force is at index 1.
# Time Complexity: O(n)
# Space Complexity: O(1)