class Solution:
    def NnumbersSum(self, N):

        if N <= 0:
            return 0
        if N == 1:
            return 1
        return N + self.NnumbersSum(N - 1)
    
''' This function calculates the sum of the first N natural numbers using recursion.
Args:
    N (int): The number up to which to calculate the sum.
'''
# Time Complexity: O(N) - where N is the number up to which the sum is calculated.
# Space Complexity: O(N) - due to the recursive call stack.

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    solution = Solution()
    result = solution.NnumbersSum(N)
    print(f"The sum of the first {N} natural numbers is: {result}")