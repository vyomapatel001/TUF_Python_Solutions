def counting_sort(arr):
    if not arr:
        return arr
    # Find the maximum element in the array
    max_val = max(arr)
    # Create a count array with a size of max_val + 1
    count = [0] * (max_val + 1)
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)): 
        sorted_arr.extend([i] * count[i])
    return sorted_arr
# Counting Sort is a non-comparison-based sorting algorithm that is efficient for sorting integers within a known range.
# Time Complexity: O(n + k) where n is the number of elements in the array and k is the range of the input.
# Space Complexity: O(k) where k is the range of the input.
if __name__ == "__main__":
    # Example usage
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Unsorted array is:")
    print(arr)
    sorted_arr = counting_sort(arr)
    print("Sorted array is:")
    print(sorted_arr)