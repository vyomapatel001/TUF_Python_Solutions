def kthpositivelement(arr, k):
    """
    Function to find the kth positive element in a sorted array.
    
    Parameters:
    arr (list): A sorted list of integers.
    k (int): The position of the positive element to find.
    
    Returns:
    int: The kth missing positive element in the array.
    """
    count = 0
    for num in range(1, max(arr) + 1):
        if num not in arr:
            count += 1
            if count == k:
                return num
    return -1  # If kth positive element does not exist

# Example usage
if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthpositivelement(arr, k))  # Output: 9

# Time Complexity: O(n * m) where n is the length of arr and m is the maximum value in arr.
# Space Complexity: O(1) since we are using a constant amount of space.

# Optimized Approach using Binary Search
def kthpositivelement(arr, k):
    """
    Function to find the kth positive element in a sorted array using binary search.
    
    Parameters:
    arr (list): A sorted list of integers.
    k (int): The position of the positive element to find.
    
    Returns:
    int: The kth positive element in the array.
    """
    left, right = 1, max(arr) + k  # Set the search range

    while left < right:
        mid = (left + right) // 2
        # Count how many positive integers are less than or equal to mid
        count = sum(1 for num in arr if num <= mid)
        
        if mid - count < k:  # If there are not enough positive integers
            left = mid + 1
        else:
            right = mid

    return left

# Example usage
if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthpositivelement(arr, k))  # Output: 9

# Time Complexity: O(n log m) where n is the length of arr and m is the maximum value in arr.
# Space Complexity: O(1) since we are using a constant amount of space.

# Optimized Approach using simple iteration
def kthpositivelement(arr, k):
    """
    Function to find the kth positive element in a sorted array using simple iteration.
    
    Parameters:
    arr (list): A sorted list of integers.
    k (int): The position of the positive element to find.
    
    Returns:
    int: The kth positive element in the array.
    """
    res = k # Start with the kth positive number
    # Iterate through the array and find the kth positive element
    for i, num in enumerate(arr):
        if num <= res:
            res += 1
        else:
            break
    return res

# Example usage
if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthpositivelement(arr, k))  # Output: 9
# Time Complexity: O(n) where n is the length of arr.
# Space Complexity: O(1) since we are using a constant amount of space.


