def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(0,n+1):
        for j in range(0,i):
            print("*", end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(i, 0, -1):
            print("*", end="")
        print()

''' This code prints a star triangle with n rows.
The first row has 1 star, the second row has 2 stars, and so on until the nth row which has n stars.
The second half of the triangle has n-1 rows, where the first row has n-1 stars, the second row has n-2 stars, and so on until the last row which has 1 star.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loops run i times,
where i goes from 0 to n-1 for the first half and from n-1 to 1 for the second half.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    nStarTriangle(n)