class Solution:
    def missingNumber(self, nums):
        """
        Find the missing number in a list of integers from 0 to n.
        :param nums: List[int] - A list containing n distinct numbers in the range [0, n].
        :return: int - The missing number.
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
# Time Complexity: O(n), where n is the length of the nums list.
# Space Complexity: O(1), as we are using a constant amount of space.
# Example usage:
solution = Solution()
nums = [0, 1, 2, 3, 5]
result = solution.missingNumber(nums)
print(result)  # Output: 4

# Second Approach:
class Solution:
    def missingNumber(self, nums):
        """
        Find the missing number in a list of integers from 0 to n using XOR.
        :param nums: List[int] - A list containing n distinct numbers in the range [0, n].
        :return: int - The missing number.
        """
        xor_sum = 0
        # Calculate XOR of all numbers from 0 to n
        # and XOR of all numbers in the list
        for i in range(len(nums) + 1):
            xor_sum ^= i 
        for num in nums:
            xor_sum ^= num
        return xor_sum
# Time Complexity: O(n), where n is the length of the nums list.
# Space Complexity: O(1), as we are using a constant amount of space.
# Example usage:
solution = Solution()
nums = [0, 1, 2, 3, 5]
result = solution.missingNumber(nums)
print(result)  # Output: 4

# Third Approach:
class Solution:
    def missingNumber(self, nums):
        """
        Find the missing number in a list of integers from 0 to n using binary search.
        :param nums: List[int] - A list containing n distinct numbers in the range [0, n].
        :return: int - The missing number.
        """
        left, right = 0, len(nums)
        # Binary search to find the missing number
        # The missing number will be at the index where nums[index] > index
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left
# Time Complexity: O(n log n), where n is the length of the nums list.
# Space Complexity: O(1), as we are using a constant amount of space.
# Example usage:
solution = Solution()
nums = [0, 1, 2, 3, 5]
result = solution.missingNumber(nums)
print(result)  # Output: 4

# Fourth Approach:
class Solution:
    def missingNumber(self, nums):
        """
        Find the missing number in a list of integers from 0 to n using set.
        :param nums: List[int] - A list containing n distinct numbers in the range [0, n].
        :return: int - The missing number.
        """
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
# Time Complexity: O(n), where n is the length of the nums list.
# Space Complexity: O(n), as we are using a set to store the numbers.
# Example usage:
solution = Solution()
nums = [0, 1, 2, 3, 5]
result = solution.missingNumber(nums)
print(result)  # Output: 4
