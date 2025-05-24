def print_name(name: str, n: int):
    # Base case: stop when n is 0
    if n == 0:
        return
    print(name)
    # Recursive call with n-1
    print_name(name, n - 1)

'''
This function prints the name a specified number of times using recursion.
Args:
    name (str): The name to print. 
    n (int): The number of times to print the name.
Returns:
    None
'''
#Time Complexity: O(n) - where n is the number of times the name is printed.
# Space Complexity: O(n) - due to the recursive call stack.


if __name__ == "__main__":
    name = input("Enter your name: ")
    times = int(input())
    print_name(name, times)
