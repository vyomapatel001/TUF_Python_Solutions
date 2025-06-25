def rotateByKElemets(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    arr[:] = arr[-k:] + arr[:-k]  # Rotate the array in place

# Example usage:
arr = [1, 2, 3, 4, 5]
rotateByKElemets(arr, 2)
print(arr)  # Output: [4, 5, 1, 2, 3]
arr = [10, 20, 30, 40, 50]
rotateByKElemets(arr, 3)
print(arr)  # Output: [30, 40, 50, 10, 20]
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are modifying the array in place without using additional space.

# Second Approach: Using slicing (not recommended for large arrays)
'''def rotateByKElemetsSlicing(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    arr[:] = arr[-k:] + arr[:-k]  # Use slicing to rotate the array
# Example usage:
arr = [1, 2, 3, 4, 5]
rotateByKElemetsSlicing(arr, 2)
print(arr)  # Output: [4, 5, 1, 2, 3]
arr = [10, 20, 30, 40, 50]
rotateByKElemetsSlicing(arr, 3)
print(arr)  # Output: [30, 40, 50, 10, 20]
# Time Complexity: O(n), where n is the number of elements in the array due to slicing.
# Space Complexity: O(n), as slicing creates a new list.
'''
# Third Approach: Using collections.deque for efficient rotation
'''from collections import deque
def rotateByKElemetsDeque(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    d = deque(arr)  # Convert the list to a deque
    d.rotate(k)  # Rotate the deque to the right by k positions
    arr[:] = list(d)  # Convert back to list and modify in place
# Example usage:
arr = [1, 2, 3, 4, 5]
rotateByKElemetsDeque(arr, 2)
print(arr)  # Output: [4, 5, 1, 2, 3]
arr = [10, 20, 30, 40, 50]
rotateByKElemetsDeque(arr, 3)
print(arr)  # Output: [30, 40, 50, 10, 20]
# Time Complexity: O(n), where n is the number of elements in the array due to deque rotation.
# Space Complexity: O(n), as we are using a deque which requires additional space.
'''
# Fourth Approach: Using reversal algorithm
'''def rotateByKElemetsReversal(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining n-k elements
    reverse(k, n - 1)

# Example usage:
arr = [1, 2, 3, 4, 5]
rotateByKElemetsReversal(arr, 2)
print(arr)  # Output: [4, 5, 1, 2, 3]
arr = [10, 20, 30, 40, 50]
rotateByKElemetsReversal(arr, 3)
print(arr)  # Output: [30, 40, 50, 10, 20]
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are modifying the array in place without using additional space.
'''