import heapq
def heap_sort(arr):
    """
    This function sorts an array using the heap sort algorithm.
    
    :param arr: List of elements to be sorted.
    :return: Sorted list of elements.
    """
    # Create a max heap from the input array
    heapq._heapify_max(arr)
    
    # Extract elements from the heap one by one
    sorted_arr = []
    while arr:
        # Pop the largest element from the heap and append it to the sorted array
        sorted_arr.append(heapq._heappop_max(arr))
    
    return sorted_arr

if __name__ == "__main__":
    # Example usage
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print(arr)

    sorted_arr = heap_sort(arr)

    print("Sorted array is")
    print(sorted_arr)
# This function implements the Heap Sort algorithm using Python's heapq module.
# It creates a max heap from the input array and then extracts elements one by one to get the sorted array.
# Time Complexity: O(n log n) for building the heap and O(n log n) for extracting elements.
# Space Complexity: O(n) for the output array, but the sorting is done in place.
# Note: The heapq module in Python provides a min-heap by default, so we use _heapify_max and _heappop_max to simulate a max-heap.
# Heap Sort is not a stable sort, meaning that it does not preserve the relative order of equal elements.
# Heap Sort is an in-place sorting algorithm, meaning it does not require additional storage for sorting.