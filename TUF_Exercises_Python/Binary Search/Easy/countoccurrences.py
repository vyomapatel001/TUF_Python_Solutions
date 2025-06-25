def countoccurrences(arr,x):
    low, high = 0, len(arr) - 1
    count = 0
    # Find the first occurrence of x
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x: # Move to the right side
            low = mid + 1 # Increase the lower bound
        elif arr[mid] > x: # Move to the left side
            high = mid - 1 # Decrease the upper bound
        else:
            count += 1 # Found an occurrence of x
            # Check for previous occurrences
            left = mid - 1 # Start checking to the left of mid
            while left >= 0 and arr[left] == x: # If the left element is equal to x
                count += 1
                left -= 1
            # Check for next occurrences
            right = mid + 1 # Start checking to the right of mid
            while right < len(arr) and arr[right] == x: # If the right element is equal to x
                count += 1
                right += 1
            break
    return count
# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 5, 2]
    x = 2
    result = countoccurrences(arr, x)
    
    print(f"The number of occurrences of {x} in the array is: {result}.")
    # Output: The number of occurrences of 2 in the array is: 3.