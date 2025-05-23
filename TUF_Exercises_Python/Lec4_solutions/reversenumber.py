class Solution:
    def reverseNumber(self, n):
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return rev

# The function reverseNumber takes an integer n as input and reverses its digits.
# It does this by repeatedly taking the last digit of n (using n % 10) and adding it to rev, which is multiplied by 10 to shift its digits left.
# The input number n is then divided by 10 to remove the last digit.
# The process continues until n becomes 0.
# The time complexity of this function is O(log n) because the number of digits in a number n is proportional to log(n).
# The space complexity is O(1) because we are using a constant amount of space for the rev variable.

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.reverseNumber(n))