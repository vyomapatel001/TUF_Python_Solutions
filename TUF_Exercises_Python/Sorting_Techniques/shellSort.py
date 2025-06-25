def shellSort(arr):
    """
    Perform shell sort on the array to sort it in ascending order.

    :param arr: List of elements to be sorted.
    """
    n = len(arr)
    gap = n // 2  # Start with a big gap, then reduce the gap

    # Do a gapped insertion sort for this gap size.
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp

        gap //= 2  # Reduce the gap for the next element

# Shell Sort is an in-place comparison sort that generalizes insertion sort to allow the exchange of items that are far apart.
# Time Complexity: O(n^(3/2)) on average, where n is the number of elements in the array.
# Space Complexity: O(1) since it uses a constant amount of space.
# Shell Sort is not a stable sort, meaning that it does not preserve the relative order of equal elements.


# Driver code to test above
arr = [ 12, 34, 54, 2, 3]

n = len(arr)
print ("Array before sorting:")
for i in range(n):
    print(arr[i]),

shellSort(arr)

print ("\nArray after sorting:")
for i in range(n):
    print(arr[i])