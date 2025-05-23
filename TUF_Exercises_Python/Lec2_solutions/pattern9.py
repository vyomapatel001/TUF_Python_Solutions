def nStarDiamond(n: int) -> None:
    # Write your code here.
    #printing the first half of the diamond
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ", end="")
        for k in range(0, 2*i+1):
            print("*", end="")
        print()
    #printing the second half of the diamond
    for i in range(n,0,-1):
        for j in range(n-i, 0, -1):
            print(" ", end="")
        for k in range(2*i-1, 0, -1):
            print("*", end="")
        print()

''' This code prints a star diamond with n rows.
The first half of the diamond has n rows, where the first row has 1 star, the second row has 3 stars, and so on until the nth row which has (2*n-1) stars.
The second half of the diamond has n rows, where the first row has (2*n-1) stars, the second row has (2*(n-1)-1) stars, and so on until the nth row which has 1 star.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loops run i times,
where i goes from 0 to n-1 for the first half and from n to 1 for the second half.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    nStarDiamond(n)