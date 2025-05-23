def getStarPattern(n: int) -> None:
    # Write your solution here.
    for i in range(0,n):
        for j in range(0,n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


''' 1. The outer loop iterates through each row of the pattern.
    2. The inner loop iterates through each column of the pattern.
    3. If the current row is the first or last row, or if the current column is the first or last column, print a star.
    4. Otherwise, print a space.
    5. After each row, print a newline character to move to the next row.
    6. The pattern is a square of size n, with stars on the border and spaces in the middle.
    7. The time complexity is O(n^2) because we are using two nested loops, each iterating n times. 
    8. The space complexity is O(1) because we are not using any additional data structures that grow with the input size.'''

if __name__ == "__main__":
    n = int(input())
    getStarPattern(n)