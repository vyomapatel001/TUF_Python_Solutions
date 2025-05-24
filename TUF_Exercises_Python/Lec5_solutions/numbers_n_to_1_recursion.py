def print_numbers(n: int):
    # Base case: stop when n is 0
    if n == 0:
        return
    # Recursive call with n-1
    
    print(n)
    print_numbers(n - 1)

''' This function prints numbers from n to 1 using recursion.
Args:
    n (int): The number from which to start printing down to 1. '''

# Time Complexity: O(n) - where n is the number from which to start printing down to 1.
# Space Complexity: O(n) - due to the recursive call stack.

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_numbers(n)