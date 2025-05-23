def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1,n+1):
        for j in range(1,i+1):
            if(i+j)%2==0:
                print("1", end="")
            else:
                print("0", end="")
        print()

''' This code prints a binary triangle with n rows.
The first row has 1 binary digit, the second row has 2 binary digits, and so on until the nth row which has n binary digits.
The binary digits are printed in a pattern where the sum of the row index and column index determines whether to print 1 or 0.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loops run i times,
where i goes from 0 to n-1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    nBinaryTriangle(n)