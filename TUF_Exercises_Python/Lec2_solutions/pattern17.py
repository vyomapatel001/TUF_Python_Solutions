def alphaHill(n: int):
    # Write your solution from here.
    for i in range(0,n):
        for j in range(0,n-i-1): #from 0 to n-i-2
            print(" ", end="") #printing spaces
        for k in range(0,i+1): #from 0 to i
            print(chr(ord('A')+k),end="") #printing A to A+i
        for l in range(i-1,-1,-1): #from i-1 to 0
            print(chr(ord('A')+l),end="") #printing A+i-1 to A
        print()

''' This code prints an alpha hill with n rows.
The first row has 1 letter, the second row has 2 letters, and so on until the nth row which has n letters.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loop runs i times,
where i goes from 0 to n-1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    alphaHill(n)
