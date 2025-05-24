class Solution:
    def reverse(self, arr, start, end):
        if start >= end:
            return arr
        # Swap the elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]
        # Recursively call reverse for the next pair
        return self.reverse(arr, start + 1, end - 1)
    
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    solution = Solution()
    reversed_arr = solution.reverse(arr, 0, len(arr) - 1)
    print("Reversed array:", reversed_arr)

# This function reverses an array using recursion.
# Time Complexity: O(n) - where n is the length of the array, as it processes each element once.
# Space Complexity: O(n) - due to the recursive call stack.
# The function swaps the first and last elements, then recursively processes the subarray excluding these two elements.