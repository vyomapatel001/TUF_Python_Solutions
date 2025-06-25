def isArraySorted(arr):
    """
    Check if the given array is sorted in non-decreasing order.
    
    :param arr: List of integers
    :return: True if the array is sorted, False otherwise
    """
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage:
print(isArraySorted([1, 2, 3, 4, 5]))  # Output: True
print(isArraySorted([3, 4, 5, 2, 1]))  # Output: False
print(isArraySorted([5, 3, 4, 2, 1]))  # Output: False
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the loop variable.
# This solution efficiently checks if the array is sorted in a single pass.

# Second Approach: Using built-in sorted function (not recommended for this problem)
'''def isArraySortedBuiltIn(arr):
    """
    Check if the given array is sorted in non-decreasing order using built-in sorted function.
    
    :param arr: List of integers
    :return: True if the array is sorted, False otherwise
    """
    return arr == sorted(arr)

#Time Complexity: O(n log n), where n is the number of elements in the array due to sorting.
# Space Complexity: O(n) for storing the sorted array.
'''
# Check if we can rotate array by few places and still have it sorted
def canRotateAndBeSorted(arr):
    """
    Check if the array can be rotated by some places and still remain sorted.
    
    :param arr: List of integers
    :return: True if the array can be rotated and remain sorted, False otherwise
    """
    n = len(arr)
    if n == 0:
        return True  # An empty array is considered sorted
    
    count = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1 # Count the number of times the current element is greater than the next element
            
    return count <= 1 # If there is at most one such occurrence, the array can be rotated and remain sorted

# Example usage:
print(canRotateAndBeSorted([3, 4, 5, 1, 2]))  # Output: True
print(canRotateAndBeSorted([1, 2, 3, 4, 5]))  # Output: True
print(canRotateAndBeSorted([5, 1, 2, 3, 4]))  # Output: True
print(canRotateAndBeSorted([3, 5, 1, 2, 4]))  # Output: False
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the count variable.
# This solution efficiently checks if the array can be rotated and remain sorted in a single pass.

# Second Approach: Using built-in sorted function (not recommended for this problem)
'''def canRotateAndBeSortedBuiltIn(arr):    
    """
    Check if the array can be rotated by some places and still remain sorted using built-in sorted function.
    
    :param arr: List of integers
    :return: True if the array can be rotated and remain sorted, False otherwise
    """
    n = len(arr)
    if n == 0:
        return True  # An empty array is considered sorted
    
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)'''
# Time Complexity: O(n log n), where n is the number of elements in the array due to sorting.
# Space Complexity: O(n) for storing the sorted array.