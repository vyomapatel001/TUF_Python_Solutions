def removeDuplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr  # If the array is empty or has only one element, return it as is
    # Initialize a new list to store unique elements
    unique_elements = []
    unique_elements.append(arr[0])  # Add the first element to the unique list
    for i in range(1, n):
        # If the current element is not equal to the last element in unique_elements, add it
        if arr[i] != arr[i - 1]:
            unique_elements.append(arr[i])
    return unique_elements  # Return the list of unique elements
# Example usage:
print(removeDuplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(removeDuplicates([1, 1, 1, 1, 1]))  # Output: [1]
print(removeDuplicates([]))  # Output: []
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(n), as we are storing the unique elements in a new list.
# This solution efficiently removes duplicates from a sorted array in a single pass.
# Note: This solution assumes the input array is sorted. If the input array is not sorted, we would need to sort it first or use a different approach.

# Second Approach: Using set to remove duplicates (not recommended for sorted arrays)
'''def removeDuplicatesSet(arr):
#     """    Remove duplicates from a sorted array using a set.
#     :param arr: List of integers (sorted)
#     :return: List of unique integers          
#     """
#     return list(set(arr))  # Convert the array to a set to remove duplicates and then back to a list
# # Example usage:
# print(removeDuplicatesSet([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# print(removeDuplicatesSet([1, 1, 1, 1, 1]))  # Output: [1]
# print(removeDuplicatesSet([]))  # Output: []
# # Time Complexity: O(n), where n is the number of elements in the array.
# # Space Complexity: O(n), as we are storing the unique elements in a set.'''

# Third Approach:
def removeDuplicatesInPlace(arr):
    """
    Remove duplicates from a sorted array in place.
    
    :param arr: List of integers (sorted)
    :return: Length of the array after removing duplicates
    """
    n = len(arr)
    if n == 0 or n == 1:
        return n  # If the array is empty or has only one element, return its length
    
    # Initialize a pointer for the position of unique elements
    j = 0
    for i in range(1, n):
        # If the current element is not equal to the last unique element, update the next position
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    return j + 1  # Return the length of the array after removing duplicates
# Example usage:
print(removeDuplicatesInPlace([1, 2, 2, 3, 4, 4, 5]))  # Output: 5
print(removeDuplicatesInPlace([1, 1, 1, 1, 1]))  # Output: 1
print(removeDuplicatesInPlace([]))  # Output: 0
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are modifying the array in place without using extra space.
# This solution efficiently removes duplicates from a sorted array in place, maintaining the order of elements.

