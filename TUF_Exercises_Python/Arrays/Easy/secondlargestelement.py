def secondLargestElement(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None

# Example usage:
print(secondLargestElement([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Output: 6
print(secondLargestElement([1, 2]))  # Output: 1
print(secondLargestElement([1]))  # Output: None
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the first and second variables.
# This solution efficiently finds the second largest element in a single pass through the array.

#Second Approach: Using sorting (not recommended for this problem)
'''def secondLargestElementSort(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    unique_elements = list(set(arr))  # Remove duplicates
    if len(unique_elements) < 2:
        return None  # Not enough unique elements for a second largest

    unique_elements.sort()  # Sort the unique elements
    return unique_elements[-2]  # Return the second last element which is the second largest

# Time Complexity: O(n log n), where n is the number of elements in the array due to sorting.
# Space Complexity: O(n) for storing unique elements in a list.'''

# Third Approach: Using built-in functions
'''def secondLargestElementBuiltIn(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    unique_elements = set(arr)  # Remove duplicates
    if len(unique_elements) < 2:
        return None  # Not enough unique elements for a second largest

    unique_elements.remove(max(unique_elements))  # Remove the largest element
    return max(unique_elements)  # Return the new largest which is the second largest
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(n) for storing unique elements in a set.'''
