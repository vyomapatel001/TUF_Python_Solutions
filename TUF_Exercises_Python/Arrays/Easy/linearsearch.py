class Solution:
    def linearSearch(self, arr, target):
        """
        Perform a linear search for the target in the array.
        :param arr: List[int] - The array to search in.
        :param target: int - The target value to search for.
        :return: int - The index of the target if found, otherwise -1.
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
# Time Complexity: O(n), where n is the length of the input array.
# Space Complexity: O(1), as we are not using any additional space.
# Example usage:
solution = Solution()
arr = [1, 2, 3, 4, 5]
target = 3
index = solution.linearSearch(arr, target)
print(index)  # Output: 2 (the index of the target value 3 in the array)