class Solution:
	def maxOnes(self, arr):
		cnt = 0
		maxi = 0
		for i in range(len(arr)):
			if arr[i]==1:
				cnt+=1
			else:
				cnt = 0
			maxi = max(maxi, cnt)
		return maxi

	
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), as we are using a constant amount of space.
# Example usage:
solution = Solution()
arr = [1, 0, 1, 1, 0, 1, 1, 1]
result = solution.maxOnes(arr)
print(result)  # Output: 3
