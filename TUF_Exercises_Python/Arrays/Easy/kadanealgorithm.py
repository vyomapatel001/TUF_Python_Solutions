import sys
def maxSubaaraySum(arr,n):
    maxi = -sys.maxsize - 1
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            maxi = max(maxi, current_sum)
    return maxi

# Kadane's Algorithm for Maximum Subarray Sum
#Time Complexity: O(n^2)
# Space Complexity: O(1)

# Second Approach: Kadane's Algorithm
def maxSubarraySum(arr, n):
    max_so_far = -sys.maxsize - 1 # Initialize to the smallest possible integer
    # Initialize current maximum to 0
    max_ending_here = 0
    
    for i in range(n):
        max_ending_here += arr[i] # Add current element to current maximum
        # Update the maximum sum found so far
        # if the current maximum is greater than the maximum found so far
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        # If current maximum becomes negative, reset it to 0
        # This is because a negative sum will not contribute to a maximum subarray sum
        if max_ending_here < 0:
            max_ending_here = 0
            
    return max_so_far
# Kadane's Algorithm is an efficient algorithm to find the maximum sum of a contiguous subarray.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Third Approach: 

# Example usage
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    maxSum = maxSubarraySum(arr, n)
    print("The maximum subarray sum is:", maxSum)
