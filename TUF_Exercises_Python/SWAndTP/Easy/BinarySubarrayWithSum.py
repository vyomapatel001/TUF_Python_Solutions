def numSubarraysWithSum(nums: list, goal: int) -> int:
    #Helper function to calculate subarrays with atmost k.
    def atMost(k:int)->int:
        if k<0: #If k is negative, subarrays are not possible
            return 0 
        
        left = 0 #Start of the sliding window
        sum_ = 0 #Current window sum
        count = 0 #Count of valid subarrays

        #Expand window by right side
        for right in range(len(nums)):
            sum_+=nums[right] # Include nums[right] in the window

            #If window sum exceeds by k, shrink it from left
            while sum_>k:
                sum_-=nums[left]
                left+=1
            
            #All subarrays between left and right are valid, calculate count
            count+= (right-left+1)
        
        return count
    #Final result = subarrays with sum ≤ goal - subarrays with sum ≤ goal - 1
    return atMost(goal) - atMost(goal-1)

if __name__ == "__main__":
    nums = [1,0,1,0,1]
    goal = 2
    print(numSubarraysWithSum(nums, goal))

    nums = [0,0,0,0,0]
    goal = 0
    print(numSubarraysWithSum(nums, goal))

#Time Complexity: O(n)
#Space Complexity: O(1)

# SeCOND aPPROACH USING PREFIX SUM AND DICTIONARY
def numSubarraysWithSum(nums: list, goal: int) -> int:
    prefix_sum = {0: 1}  # Initialize with sum 0 having one occurrence
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num  # Update the current prefix sum

        # Check if there is a prefix sum that would give us the desired subarray sum
        if (current_sum - goal) in prefix_sum:
            count += prefix_sum[current_sum - goal]

        # Update the count of the current prefix sum
        if current_sum in prefix_sum:
            prefix_sum[current_sum] += 1
        else:
            prefix_sum[current_sum] = 1

    return count

if __name__ == "__main__":
    nums = [1,0,1,0,1]
    goal = 2
    print(numSubarraysWithSum(nums, goal))  # Output: 4

    nums = [0,0,0,0,0]
    goal = 0
    print(numSubarraysWithSum(nums, goal))  # Output: 15

# Time Complexity: O(n)
# Space Complexity: O(n) for storing the prefix sums in the dictionary
# This approach uses a dictionary to keep track of the prefix sums and their counts, allowing us to efficiently find the number of subarrays that sum to the desired goal.
# It iterates through the array once, updating the current prefix sum and checking for the required prefix sums to count valid subarrays.

# This approach is efficient and avoids the need for nested loops, making it suitable for larger input sizes.

# Third Approach using defaultdict for cleaner code
from collections import defaultdict

def numSubarraysWithSum(nums: list, goal: int) -> int:
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        # Check if there is a prefix sum that would give us the desired subarray sum
        if (current_sum - goal) in prefix_sum:
            count += prefix_sum[current_sum - goal]

        # Update the count of the current prefix sum
        prefix_sum[current_sum] += 1

    return count

if __name__ == "__main__":
    nums = [1,0,1,0,1]
    goal = 2
    print(numSubarraysWithSum(nums, goal))  # Output: 4

    nums = [0,0,0,0,0]
    goal = 0
    print(numSubarraysWithSum(nums, goal))  # Output: 15

# Time Complexity: O(n)
# Space Complexity: O(n) for storing the prefix sums in the dictionary
