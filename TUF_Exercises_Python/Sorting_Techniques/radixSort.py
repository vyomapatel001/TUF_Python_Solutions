def counting_sort(arr, exp):
    """
    A function to perform counting sort on the array based on the digit represented by exp.
    
    :param arr: List of elements to be sorted.
    :param exp: The exponent representing the digit to be sorted (1 for units, 10 for tens, etc.).
    """
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits 0-9

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Perform radix sort on the array to sort it in ascending order.
    
    :param arr: List of elements to be sorted.
    """
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit
    exp = 1  # Exponent representing the current digit (1 for units, 10 for tens, etc.)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next digit

# Radix Sort is a non-comparison-based sorting algorithm that sorts numbers by processing individual digits.
# Time Complexity: O(d * (n + k)), where d is the number of digits in the maximum number, n is the number of elements in the array, and k is the range of the input.
# Space Complexity: O(n) for the output array.

if __name__ == "__main__":
    # Example usage
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Unsorted array is:")
    print(arr)
    radix_sort(arr)
    print("Sorted array is:")
    print(arr)