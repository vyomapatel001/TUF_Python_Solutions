class Solution:
    def largestElement(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return None  # Handle empty list case
        # Initialize max_element with the first element of the array
        max_element = arr[0]
        # Iterate through the array to find the largest element
        for num in arr:
            # Compare each element with the current max_element
            if num > max_element:
                max_element = num # Update max_element if a larger number is found
        return max_element
    
#Second Approach: Using built-in max function

''' def largestElementBuiltIn(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return None  # Handle empty list case
        return max(arr)  # Use built-in max function to find the largest element
        
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the max_element variable.  

'''

# Third Approach: Using sorting (not recommended for this problem)
'''def largestElementSort(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return None  # Handle empty list case
        arr.sort()  # Sort the array in ascending order
        return arr[-1]  # Return the last element which is the largest

        # Note: This approach has a higher time complexity due to sorting.

        # Time Complexity: O(n log n), where n is the number of elements in the array.
        # Space Complexity: O(1) if we sort in place, but O(n) if we create a new sorted array.'''
    
# Example usage:
sol = Solution()
print(sol.largestElement([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Output: 9
print(sol.largestElement([]))  # Output: None

# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the max_element variable.