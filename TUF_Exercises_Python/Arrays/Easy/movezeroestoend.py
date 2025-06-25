class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1
        for i in range(zero_index, len(nums)):
            nums[i] = 0
        # The first loop moves all non-zero elements to the front,
        # and the second loop fills the rest of the array with zeros.
        # This ensures that all zeros are moved to the end of the array.
# Time Complexity: O(n), where n is the length of the input array.
# Space Complexity: O(1), as we are modifying the array in-place without using extra space.
# Example usage:
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

# Second Approach:
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for num in nums:
            if num != 0:
                temp.append(num)
        zero_count = len(nums) - len(temp)
        nums[:] = temp + [0] * zero_count
# Time Complexity: O(n), where n is the length of the input array.
# Space Complexity: O(n), as we are using an additional list to store non-zero elements.
# Example usage:
solution = Solution()
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
