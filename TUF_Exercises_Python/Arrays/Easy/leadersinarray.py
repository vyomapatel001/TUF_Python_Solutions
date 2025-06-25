def printLeadersBruteForce(arr, n):
    """
    Function to find all leaders in the array.
    A leader is an element that is greater than all elements to its right.

    :param arr: List of integers.
    :param n: Length of the array.
    :return: List of leaders in the array.
    """
    leaders = []
    
    for i in range(n):
        is_leader = True
        for j in range(i + 1, n):
            if arr[i] <= arr[j]:
                is_leader = False
                break
        if is_leader:
            leaders.append(arr[i])
    
    return leaders

# Second Approach: Optimized Approach
def printLeadersOptimized(arr, n):
    """
    Function to find all leaders in the array using an optimized approach.
    A leader is an element that is greater than all elements to its right.

    :param arr: List of integers.
    :param n: Length of the array.
    :return: List of leaders in the array.
    """
    leaders = []
    max_from_right = arr[-1] # Initialize the last element as the first leader
    leaders.append(max_from_right) # Add the last element as a leader
    # Traverse the array from right to left

    for i in range(n - 2, -1, -1): # Start from the second last element
    # Check if the current element is greater than the maximum from the right
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    return leaders[::-1]  # Reverse to maintain original order

# Optimized Approach is more efficient as it only traverses the array once from right to left.
## Time Complexity: O(n)
# Space Complexity: O(n) for storing leaders


# Main function
if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeadersBruteForce(arr, n)

    for i in range(len(ans)):
        print(ans[i], end=" ")

    print()