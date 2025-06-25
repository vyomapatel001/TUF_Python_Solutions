def maxProductofSubarray(arr):
    if not arr:
        return 0

    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        
        result = max(result, max_product)

    return result
# Example usage
if __name__ == "__main__":
    arr = [2, 3, -2, 4]
    print("Maximum product of subarray is:", maxProductofSubarray(arr))
# This function calculates the maximum product of a contiguous subarray.
# Time Complexity: O(n) where n is the number of elements in the array.
# Space Complexity: O(1) since we are using a constant amount of space.
# The algorithm keeps track of the maximum and minimum products at each step, as a negative number can turn a small product into a large one.
# The result is updated with the maximum product found so far.
# The function handles edge cases such as empty arrays and arrays with negative numbers.
# The function returns the maximum product of any contiguous subarray within the given array.
# The maximum product subarray problem is a common interview question and can be solved efficiently using dynamic programming techniques.
# The function is designed to handle both positive and negative integers, ensuring that the maximum product is calculated correctly.

# Second Approach: Using Dynamic Programming
def maxProductofSubarrayDP(arr):
    if not arr:
        return 0

    n = len(arr)
    dp_max = [0] * n
    dp_min = [0] * n
    dp_max[0] = arr[0]
    dp_min[0] = arr[0]
    result = arr[0]

    for i in range(1, n):
        if arr[i] < 0:
            dp_max[i] = max(arr[i], dp_min[i-1] * arr[i])
            dp_min[i] = min(arr[i], dp_max[i-1] * arr[i])
        else:
            dp_max[i] = max(arr[i], dp_max[i-1] * arr[i])
            dp_min[i] = min(arr[i], dp_min[i-1] * arr[i])
        
        result = max(result, dp_max[i])

    return result