class Solution:
    def countDigit(self, n):
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count
# The function countDigit counts the number of digits in a given integer n.
# It does this by repeatedly dividing n by 10 until n becomes 0, incrementing the count each time.
# The time complexity of this function is O(log n) because the number of digits in a number n is proportional to log(n).
# The space complexity is O(1) because we are using a constant amount of space for the count variable.

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.countDigit(n))