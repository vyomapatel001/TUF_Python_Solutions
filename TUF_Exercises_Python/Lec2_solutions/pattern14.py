def nLetterTriangle(n: int) -> None:
    # Write your solution here.

    for i in range(0, n):
        for j in range(0,i+1):
            print(chr(ord('A') + j), end="")
        print()

''' This code prints a letter triangle with n rows.
The first row has 0 letters, the second row has 1 letter, and so on until the nth row which has (n-1) letters.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loop runs i times,
where i goes from 0 to n-1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    nLetterTriangle(n)
