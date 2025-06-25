def singleNonDuplicateElement(arr):
    """
    This function finds the single non-duplicate element in a sorted array where every other element appears twice.
    
    :param arr: List[int] - A sorted list of integers where every element except one appears twice.
    :return: int - The single non-duplicate element.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Ensure mid is even
        if mid % 2 == 1: 
            mid -= 1 # Adjust mid to be even
        
        # Check if the pair matches
        if arr[mid] == arr[mid + 1]: # If the pair matches, the single element is in the right half
            left = mid + 2 # Move to the right half
        # If the pair does not match, the single element is in the left half or at mid
        else:
            right = mid
    # If we exit the loop, left should point to the single non-duplicate element        
    return arr[left]

# Example usage
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    result = singleNonDuplicateElement(arr)
    print(f"The single non-duplicate element is: {result}")
    # Output: The single non-duplicate element is: 5
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Note: The input array must be sorted and contain exactly one non-duplicate element.

# bRUTE Force Approach : XOR
def singleNonDuplicateElementXOR(arr):
    """
    This function finds the single non-duplicate element in a sorted array using XOR.
    
    :param arr: List[int] - A sorted list of integers where every element except one appears twice.
    :return: int - The single non-duplicate element.
    """
    result = 0
    for num in arr:
        result ^= num
    return result
# Example usage for XOR approach
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    result = singleNonDuplicateElementXOR(arr)
    print(f"The single non-duplicate element using XOR is: {result}")
    # Output: The single non-duplicate element using XOR is: 5
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: The XOR approach works for any array where every element except one appears twice, not necessarily sorted.
# The XOR approach is more general and can be applied to unsorted arrays as well.
# However, the binary search approach is more efficient for sorted arrays.