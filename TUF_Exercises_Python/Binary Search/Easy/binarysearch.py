# Iterative Binary Search in Python
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binarySearch(arr, target)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Recursive Binary Search in Python
def binarySearchRecursive(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            return binarySearchRecursive(arr, mid + 1, right, target)
        # If target is smaller, ignore right half
        else:
            return binarySearchRecursive(arr, left, mid - 1, target)

    # Target was not found in the array
    return -1

# Example usage for recursive binary search
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binarySearchRecursive(arr, 0, len(arr) - 1, target)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")