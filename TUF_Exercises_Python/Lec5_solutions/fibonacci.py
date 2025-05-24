class Solution:
    def fib(self, n):
        #your code goes here
        if n==0 or n==1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    print("Fibonacci series:")
    for i in range(n):
        print(solution.fib(i), end=" ")
    print()

# This function calculates the nth Fibonacci number using recursion.
# Time Complexity: O(2^n) - due to the exponential growth of recursive calls.
# Space Complexity: O(n) - due to the recursive call stack.