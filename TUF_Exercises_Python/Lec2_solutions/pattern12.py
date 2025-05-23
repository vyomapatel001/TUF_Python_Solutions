def numberCrown(n: int) -> None:
    # Write your solution here.
    for i in range(1,n+1):
        #printing from 1 to i
        for j in range(1,i+1):
            print(j, end="")

        #printing spaces
        spaces =  " " * 2*(n-i)
        print(spaces, end="")

        #printing from i to 1
        for j in range(i, 0, -1):
            print(j, end="")
        print()

''' This code prints a number crown with n rows.
The first row has 1 number, the second row has 2 numbers, and so on until the nth row which has n numbers.
The second half of the crown has n rows, where the first row has n numbers, the second row has (n-1) numbers, and so on until the last row which has 1 number.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loops run i times,
where i goes from 1 to n for the first half and from n to 1 for the second half.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''

if __name__ == "__main__":
    n = int(input())
    numberCrown(n)

