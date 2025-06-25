import sys
def findKRotation(arr : [int]) -> int:
    low = 0
    high = len(arr) - 1
    ans = float('inf')
    index = -1
    while low <= high:
        mid = (low + high) // 2

        # If search space is already sorted,
        # then arr[low] will always be
        # the minimum in that search space
        if arr[low] <= arr[high]: # If the array is already sorted
            if arr[low] < ans:
                index = low
                ans = arr[low]
            break

        # If left part is sorted
        if arr[low] <= arr[mid]:
            # Keep the minimum
            if arr[low] < ans:
                index = low
                ans = arr[low]

            # Eliminate left half
            low = mid + 1
        else:  # If right part is sorted
            # Keep the minimum
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]

            # Eliminate right half
            high = mid - 1

    return index


# Example usage
if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    result = findKRotation(arr)
    
    print(f"The array is rotated {result} times.")
# Output: The array is rotated 2 times.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Brute Force Approach
def numberOfTimesArrayRotatedBruteForce(arr, n):
    """
    Find the number of times a sorted array has been rotated.
    
    :param arr: List[int] - A sorted list of integers that has been rotated.
    :param n: int - The length of the array.
    :return: int - The number of times the array has been rotated.
    """
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return i
    return 0

# Example usage for brute force approach
if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    result = numberOfTimesArrayRotatedBruteForce(arr, n)
    
    print(f"The array is rotated {result} times using brute force.")
# Output: The array is rotated 2 times using brute force.
# Time Complexity: O(n)
# Space Complexity: O(1)
# The brute force approach is less efficient than the binary search approach, especially for large arrays.