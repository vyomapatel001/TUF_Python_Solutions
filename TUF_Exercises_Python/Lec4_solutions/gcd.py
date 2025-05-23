class Solution:
    def GCD(self, n1, n2):
        # Base case: if n2 is 0, return n1
        if n2 == 0:
            return n1
        # Recursive case: call GCD with n2 and the remainder of n1 divided by n2
        return self.GCD(n2, n1 % n2)
    
# Time Complexity: O(log(min(n1, n2))) because the algorithm reduces the problem size by at least half in each recursive call.
# Space Complexity: O(log(min(n1, n2))) due to the recursion stack space used in the function calls.



if __name__ == "__main__":
    n1, n2 = map(int, input().split())
    obj = Solution()
    print(obj.GCD(n1, n2))