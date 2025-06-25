def countSubArraySumEqualsK(arr, k):
    count = 0
    n = len(arr)
    
    # Iterate through all subarrays
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == k:
                count += 1
                
    return count

# Second Approach: Using HashMap
def countSubArraySumEqualsKOptimized(arr, k):
    count = 0
    current_sum = 0
    sum_map = {0: 1}  # Initialize with sum 0 having one occurrence
    
    for num in arr:
        current_sum += num
        
        # Check if (current_sum - k) exists in the map
        if (current_sum - k) in sum_map:
            count += sum_map[current_sum - k]
        
        # Update the map with the current sum
        if current_sum in sum_map:
            sum_map[current_sum] += 1
        else:
            sum_map[current_sum] = 1
            
    return count

# Optimized Approach is more efficient as it uses a HashMap to store the cumulative sums.
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(n) for storing the cumulative sums in the HashMap.

# Third Approach: Using Prefix Sum
def countSubArraySumEqualsKPrefix(arr, k):
    count = 0
    prefix_sum = [0] * (len(arr) + 1)
    
    # Calculate prefix sums
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    # Count subarrays with sum equal to k
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if prefix_sum[j] - prefix_sum[i] == k:
                count += 1
                
    return count

# time Complexity: O(n^2) where n is the length of the array.
# Space Complexity: O(n) for storing the prefix sums.

# Fourth Approach: Using Sliding Window (only for non-negative integers)
def countSubArraySumEqualsKSlidingWindow(arr, k):
    count = 0
    current_sum = 0
    left = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink the window from the left if the current sum exceeds k
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
            
        # If current sum equals k, increment count
        if current_sum == k:
            count += 1
            
    return count
# Sliding Window is efficient for non-negative integers.
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) as we are using a fixed number of variables.

# Fifth Approach: Using defaultdict from collections
from collections import defaultdict

def countSubArraySumEqualsKDefaultDict(arr, k):
    count = 0
    current_sum = 0
    sum_map = defaultdict(int)  # Initialize with default value of 0
    sum_map[0] = 1  # To handle the case when subarray starts from index 0
    
    for num in arr:
        current_sum += num
        
        # Check if (current_sum - k) exists in the map
        if (current_sum - k) in sum_map:
            count += sum_map[current_sum - k]
        
        # Update the map with the current sum
        sum_map[current_sum] += 1
            
    return count

# This function counts the number of subarrays whose sum equals k.
#Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(n) for storing the cumulative sums in the defaultdict.
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 5
    count = countSubArraySumEqualsK(arr, k)
    print("Number of subarrays with sum equal to", k, "is:", count) # Output: 2