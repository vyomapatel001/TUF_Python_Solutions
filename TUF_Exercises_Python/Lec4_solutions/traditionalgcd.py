class Solution:
    def GCD(self, n1, n2):
        while n2!=0:
            n1,n2 = n2,n1%n2 #Euclid's algorithm
        return n1

# Time Complexity: O(log(min(n1, n2))) because the algorithm reduces the problem size by at least half in each iteration.
# Space Complexity: O(1) because we are using a constant amount of space for the variables n1 and n2.
if __name__ == "__main__":
    n1, n2 = map(int, input().split())
    obj = Solution()
    print(obj.GCD(n1, n2))