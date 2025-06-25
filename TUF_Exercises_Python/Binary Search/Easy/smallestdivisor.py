# Brute Force Approach
def smallestDivisor(nums, threshold):
    n = len(nums)
    maxi = max(nums)

    for i in range(1, maxi + 1):
        total = 0
        for j in range(n):
            total += (nums[j] + i - 1) // i # Equivalent to ceil(nums[j] / i)
        if total <= threshold:
            return i
    return -1  # In case no divisor is found, though the problem guarantees a solution.

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 5, 9]
    threshold = 6
    print(smallestDivisor(nums, threshold))  # Output: 5

# Time Complexity: O(n * m) where n is the length of nums and m is the maximum value in nums.
# Space Complexity: O(1) since we are using a constant amount of space.

# Optimized Approach using Binary Search
def smallestDivisor(nums, threshold):
    # Function to check if a divisor is valid
    def isValid(divisor):
        total = sum((num + divisor - 1) // divisor for num in nums) # Equivalent to ceil(num / divisor)
        # Check if the total is within the threshold
        return total <= threshold
    # Binary search for the smallest divisor
    left, right = 1, max(nums)

    while left < right:
        mid = (left + right) // 2
        if isValid(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 5, 9]
    threshold = 6
    print(smallestDivisor(nums, threshold))  # Output: 5
# Time Complexity: O(n log m) where n is the length of nums and m is the maximum value in nums.
# Space Complexity: O(1) since we are using a constant amount of space.
