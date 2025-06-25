from collections import Counter
def counting_sort(arr):
    """
    Perform counting sort on the array to sort it in ascending order.

    :param arr: List of elements to be sorted.
    :return: Sorted list of elements.
    """
    if not arr:
        return arr
    
    # Count the occurrences of each element
    count = Counter(arr)
    
    # Create a sorted list based on the counts
    sorted_arr = []
    for num in sorted(count.keys()):
        sorted_arr.extend([num] * count[num])
    
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
