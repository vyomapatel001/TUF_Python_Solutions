def searchInsertPosition(nums, target):
    """
    Find the index at which the target should be inserted in a sorted array.
    
    :param nums: List[int] - A sorted list of integers.
    :param target: int - The target value to find the insert position for.
    :return: int - The index where the target can be inserted.
    """
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        
        # If target is found, return the index
        if nums[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif nums[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
    # If target is not found, return the index where it can be inserted
    if target not in nums:
        if target > nums[high]:
            return high + 1
        else:
            return low

# Example usage
if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    result = searchInsertPosition(nums, target)
    
    print(f"The target {target} can be inserted at index {result}.")
    # Output: The target 5 can be inserted at index 2.
    
    target = 2
    result = searchInsertPosition(nums, target)
    
    print(f"The target {target} can be inserted at index {result}.")
    # Output: The target 2 can be inserted at index 1.
    
    target = 7
    result = searchInsertPosition(nums, target)
    
    print(f"The target {target} can be inserted at index {result}.")
    # Output: The target 7 can be inserted at index 4.
    
    target = 0
    result = searchInsertPosition(nums, target)
    
    print(f"The target {target} can be inserted at index {result}.")
    # Output: The target 0 can be inserted at index 0.

# Time Complexity: O(log n)
# Space Complexity: O(1)
# The function uses binary search to find the appropriate index for the target.