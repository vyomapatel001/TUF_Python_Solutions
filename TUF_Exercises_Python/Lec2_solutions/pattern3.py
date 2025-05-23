def nTriangle(n:int) ->None:
    # Write your solution here.
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print()

''' This code prints a right-angled triangle of numbers with n rows.
The first row has 1, the second row has 12, the third row has 123, and so on until the nth row which has 123...n.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loop runs i times,
where i goes from 1 to n.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''

if __name__ == "__main__":
    n = int(input())
    nTriangle(n)