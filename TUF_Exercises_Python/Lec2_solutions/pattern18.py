def alphaTriangle(n: int):
    # Write your solution here.
    for i in range(0,n): # 0 to n-1
        # For each row, print the letters in reverse order
        for j in range(i,-1,-1): # i to 0
            print(chr(ord('A') + n-j-1), end="")
        print()

#Time complexity is O(n^2) because the outer loop runs n times and the inner loop runs i times,
#Space complexity is O(1) because we are not using any additional data structures that grow with the input size.

if __name__ == "__main__":
    n = int(input())
    alphaTriangle(n)