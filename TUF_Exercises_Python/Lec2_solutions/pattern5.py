def seeding(n: int) -> None:
    # Write your solution here.
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print("*", end="")
        print()

''' This code prints an inverted right-angled triangle of stars with n rows.
The first row has n stars, the second row has n-1 stars, and so on until the nth row which has 1 star.
The time complexity of the above code is O(n^2) because the outer loop runs n times and the inner loop runs i times,
where i goes from n to 1.
The space complexity is O(1) because we are not using any additional data structures that grow with the input size. '''
if __name__ == "__main__":
    n = int(input())
    seeding(n)