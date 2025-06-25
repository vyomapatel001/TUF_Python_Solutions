def heapify(arr, n, i):
    largest = i #Initialize largest as root
    left = 2 * i + 1 # left = 2*i + 1
    right = 2 * i + 2 # right = 2*i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > largest:
        largest = right
    
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap root with largest
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree

def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2, -1,-1):
        heapify(arr,n,i)
    
    # One by one extract elements from heap
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    # Example usage
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print(arr)

    heapSort(arr)

    print("Sorted array is")
    print(arr)
# This function implements the Heap Sort algorithm to sort an array in ascending order.
# It builds a max heap from the array and then extracts elements one by one to get the sorted array.
# Time Complexity: O(n log n) for building the heap and O(n log n) for extracting elements.
# Space Complexity: O(1) as it sorts the array in place.
