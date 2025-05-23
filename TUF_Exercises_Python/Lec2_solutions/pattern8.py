def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n, 0, -1):
        #printing spaces
        for j in range(n-i, 0, -1):
            print(" ", end="")
        #printing stars
        for k in range(2*i-1, 0, -1):
            print("*", end="")
        print()

''' This code prints a star triangle with n rows.
The first row has (2*n-1) stars, the second row has (2*(n-1)-1) stars, and so on until the nth row which has 1 star.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loops run i times,
where i goes from n to 1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    nStarTriangle(n)