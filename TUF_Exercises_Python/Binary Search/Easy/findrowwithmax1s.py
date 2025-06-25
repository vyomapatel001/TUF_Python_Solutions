def rowWithMax1s(matrix):
    max_row_index = -1
    max_count = -1
    
    for i in range(len(matrix)):
        count = sum(matrix[i])
        if count > max_count:
            max_count = count
            max_row_index = i
            
    return max_row_index

# Example usage
if __name__ == "__main__":
    matrix = [
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    print(rowWithMax1s(matrix))  # Output: 2
# Time Complexity: O(n * m) where n is the number of rows and m is the number of columns in the matrix.
# Space Complexity: O(1) since we are using a constant amount of space.

# Optimized Approach
def rowWithMax1s(matrix):
    max_row_index = -1
    max_count = -1
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    
    j = m - 1  # Start from the last column
    
    for i in range(n):
        while j >= 0 and matrix[i][j] == 1: # Move left while we find 1s
            j -= 1 # Update the max_row_index if we find more 1s
            max_row_index = i # Update the max_count
            max_count += 1 
            
    return max_row_index

# Example usage
if __name__ == "__main__":
    matrix = [
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    print(rowWithMax1s(matrix))  # Output: 2
# Time Complexity: O(n + m) where n is the number of rows and m is the number of columns in the matrix.
# Space Complexity: O(1) since we are using a constant amount of space.

# Binary Search Approach
def rowWithMax1s(matrix):
    max_row_index = -1
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    
    for i in range(n):
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[i][mid] == 1:
                max_row_index = i
                left = mid + 1
            else:
                right = mid - 1
                
    return max_row_index

# Example usage
if __name__ == "__main__":
    matrix = [
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    print(rowWithMax1s(matrix))  # Output: 2
# Time Complexity: O(n log m) where n is the number of rows and m is the number of columns in the matrix.
# Space Complexity: O(1) since we are using a constant amount of space.