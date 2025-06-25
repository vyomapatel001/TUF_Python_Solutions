def leftRotate(arr):
    """
    Rotate the array to the left by one position.
    
    :param arr: List of integers
    :return: None (the array is modified in place)
    """
    if not arr:
        return  # Handle empty array case
    
    first_element = arr[0]  # Store the first element
    n = len(arr)
    
    # Shift all elements to the left
    for i in range(1, n):
        arr[i - 1] = arr[i]
    
    arr[n - 1] = first_element  # Place the first element at the end

# Example usage:
arr = [1, 2, 3, 4, 5]
leftRotate(arr)
print(arr)  # Output: [2, 3, 4, 5, 1]
arr = [10, 20, 30]
leftRotate(arr)
print(arr)  # Output: [20, 30, 10]
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are modifying the array in place without using additional space.

# Second Approach: Using slicing (not recommended for large arrays)
'''def leftRotateSlicing(arr):
    """
    Rotate the array to the left by one position using slicing.
    
    :param arr: List of integers
    :return: None (the array is modified in place)
    """
    if not arr:
        return  # Handle empty array case
    
    arr[:] = arr[1:] + arr[:1]  # Use slicing to rotate the array
# Example usage:
arr = [1, 2, 3, 4, 5]
leftRotateSlicing(arr)
print(arr)  # Output: [2, 3, 4, 5, 1]
arr = [10, 20, 30]

leftRotateSlicing(arr)
print(arr)  # Output: [20, 30, 10]
# Time Complexity: O(n), where n is the number of elements in the array due to slicing.
# Space Complexity: O(n), as slicing creates a new list.
'''
# Third Approach: Using collections.deque for efficient rotation
'''from collections import deque
def leftRotateDeque(arr):
    """
    Rotate the array to the left by one position using collections.deque.
    
    :param arr: List of integers
    :return: None (the array is modified in place)
    """
    if not arr:
        return  # Handle empty array case
    
    d = deque(arr)  # Convert the list to a deque
    d.rotate(-1)  # Rotate the deque to the left by one position
    arr[:] = list(d)  # Convert back to list and modify in place

# Example usage:
arr = [1, 2, 3, 4, 5]
leftRotateDeque(arr)
print(arr)  # Output: [2, 3, 4, 5, 1]
arr = [10, 20, 30]
leftRotateDeque(arr)
print(arr)  # Output: [20, 30, 10]
# Time Complexity: O(n), where n is the number of elements in the array due to deque rotation.
# Space Complexity: O(n), as we are using a deque which requires additional space.
'''