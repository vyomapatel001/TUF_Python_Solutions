def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    num = 1
    for i in range(1,n+1):
        for j in range(1,i+1): #from 1 to i 
            print(num, end="") #printing num
            num+=1 #incrementing num by 1
        print()

''' This code prints a number triangle with n rows.
The first row has 1 number, the second row has 2 numbers, and so on until the nth row which has n numbers.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loop runs i times,
where i goes from 1 to n.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''

if __name__ == "__main__":
    n = int(input())
    nNumberTriangle(n)