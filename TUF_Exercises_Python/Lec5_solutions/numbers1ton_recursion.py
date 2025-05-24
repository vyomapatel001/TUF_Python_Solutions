def print_numbers(n: int):
    # Base case: stop when n is 0
    if n == 0:
        return
    # Recursive call with n-1
    print_numbers(n - 1)
    print(n)



''' This function prints numbers from 1 to n using recursion.
Args:
    n (int): The number up to which to print.
Returns:
    None
'''
# Time Complexity: O(n) - where n is the number up to which numbers are printed.
# Space Complexity: O(n) - due to the recursive call stack.

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_numbers(n)