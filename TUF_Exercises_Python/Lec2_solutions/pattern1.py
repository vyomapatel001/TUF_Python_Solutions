def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(0,n): #Outer loop runs n times
        #Inner loop runs n times
        for j in range(0,n):
            print("*", end="")
        print()

# The above code prints a square of stars with n rows and n columns.
# The time complexity of the above code is O(n^2) because there are two nested loops, each running n times.
# The space complexity is O(1) because we are not using any additional data structures that grow with the input size.

if __name__ == "__main__":
    n = int(input())
    nForest(n)