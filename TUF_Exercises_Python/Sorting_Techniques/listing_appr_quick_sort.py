def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x<= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    
if __name__ == "__main__":
    # Example usage
    arr = [1, 7, 4, 1, 10, 9, -2]
    print("Given array is")
    print(arr)

    sorted_arr = quicksort(arr)
    
    print("Sorted array is")
    print(sorted_arr)

# This function implements the QuickSort algorithm to sort an array in ascending order.
# It uses recursion to divide the array into smaller subarrays based on a pivot element.
# Time Complexity: O(n log n) on average, O(n^2) in the worst case.
# Space Complexity: O(log n) due to the recursive stack space.