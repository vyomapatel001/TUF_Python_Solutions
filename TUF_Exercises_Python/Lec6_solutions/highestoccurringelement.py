class Solution:
    def mostFrequentElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        most_frequent = max(frequency, key=frequency.get)
        least_frequent = min(frequency, key=frequency.get)
        return f"{most_frequent} {least_frequent}"
    
if __name__ == "__main__":
    # Example usage
    nums = [4, 4, 5, 5, 6]
    solution = Solution()
    print(solution.mostFrequentElement(nums))  # Output: 1

# This function finds the most and least frequently occurring elements in the list nums.
# Time Complexity: O(n) - where n is the length of nums, as it processes each element in nums once to build the frequency dictionary.
# Space Complexity: O(n) - for storing the frequency counts in the dictionary.
# Note: The function returns a string with the most and least frequent elements separated by a space.