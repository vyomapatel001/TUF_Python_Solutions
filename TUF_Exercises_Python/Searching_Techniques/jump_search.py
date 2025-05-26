def jump_search(arr, target):
    """
    Perform a jump search on the sorted array to find the target element.

    :param arr: Sorted list of elements to search in.
    :param target: Element to search for.
    :return: Index of the target element if found, otherwise -1.
    """
    n = len(arr)
    step = int(n**0.5)  # Calculate the optimal jump size
    prev = 0

    # Finding the block where the target is present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1  # Target is not present in the array

    # Linear search within the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1  # Target is not present in the array

    # If the element is found
    if arr[prev] == target:
        return prev

    return -1  # Return -1 if the target is not found in the array

if __name__ == "__main__":
    # Example usage
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = jump_search(sorted(arr), target)
    if result != -1:
        print(f"Jump Search: Element found at index {result}")
    else:
        print("Jump Search: Element not found")

# Jump Search is a searching algorithm for sorted arrays that works by jumping ahead by fixed steps and then performing a linear search within the identified block.
# Time Complexity: O(√n) where n is the number of elements in the array.
# Space Complexity: O(1) since it uses a constant amount of space.

