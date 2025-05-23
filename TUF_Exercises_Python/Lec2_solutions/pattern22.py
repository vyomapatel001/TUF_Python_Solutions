def print_pattern(N):
    for i in range(2*N-1):
        for j in range(2*N-1):
            val = N - min(i, j, 2*N-2-i, 2*N-2-j)
            print(val, end=" ")
        print()

# The function print_pattern prints a pattern of numbers in a square grid.
# The pattern consists of concentric squares, where the outermost square has the value N, and each inner square has a value that decreases by 1.
# The pattern is symmetric and has a size of (2*N-1) x (2*N-1).
# The time complexity of this function is O(N^2) because we have two nested loops, each iterating (2*N-1) times.
# The space complexity is O(1) because we are not using any additional data structures that grow with the input size.

if __name__ == "__main__":
    N = int(input())
    print_pattern(N)