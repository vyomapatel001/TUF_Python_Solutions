def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()

''' This code prints a right-angled triangle of numbers with n rows.
The first row has 123...n, the second row has 123...(n-1), and so on until the nth row which has 1.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loop runs i times,
where i goes from n to 1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''

if __name__ == "__main__":
    n = int(input())
    nNumberTriangle(n)