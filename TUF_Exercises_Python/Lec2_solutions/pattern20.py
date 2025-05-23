def symmetry(n: int):
    # Write your solution from here.

    # Print the lower half of the pattern
    for i in range(1,n+1):
        # Print the left half of the pattern
        for j in range(1,i+1):
            print("*", end="")
        # Print the spaces in the middle
        spaces = " "*2*(n-i)
        print(spaces, end="")
        # Print the right half of the pattern
        for k in range(i,0,-1):
            print("*", end="")
        print()

    # Print the upper half of the pattern
    for i in range(n-1,0,-1):
        # Print the left half of the pattern
        for j in range(1,i+1):
            print("*", end="")
        # Print the spaces in the middle
        spaces = " " * (2*(n-i))
        print(spaces, end="")
        # Print the right half of the pattern
        for k in range(i,0,-1):
            print("*", end="")
        print()
        

if __name__ == "__main__":
    n = int(input())
    symmetry(n)
