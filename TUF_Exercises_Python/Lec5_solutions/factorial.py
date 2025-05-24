def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    :param n: Non-negative integer for which to calculate the factorial
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer: "))
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")
    except ValueError as e:
        print(e)
# This function calculates the factorial of a non-negative integer n using recursion.

#Time Complexity: O(n) - where n is the input number, as it makes n recursive calls.
#Space Complexity: O(n) - due to the recursive call stack.
# The factorial of 0 is defined as 1, and the factorial of 1 is also 1.