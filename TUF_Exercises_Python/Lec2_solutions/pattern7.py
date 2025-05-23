def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(0,n):
        #printing spaces
        for j in range(0, n-i-1):
            print(" ", end="")
        #printing stars
        for j in range(0,(2*i)+1):
            print("*", end="")
        print()

''' This code prints a star triangle with n rows.
The first row has 1 star, the second row has 3 stars, and so on until the nth row which has (2*n-1) stars.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loops run i times,
where i goes from 0 to n-1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    nStarTriangle(n)   