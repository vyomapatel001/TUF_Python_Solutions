class Solution:
    def isPalindrome(self, n):
        rev = 0
        original = n
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return original == rev

# The function isPalindrome checks if a given integer n is a palindrome.
# A palindrome is a number that reads the same backward as forward.
# The function reverses the number by repeatedly taking the last digit of n (using n % 10) and adding it to rev, which is multiplied by 10 to shift its digits left.
# The input number n is then divided by 10 to remove the last digit.
# The process continues until n becomes 0.
# Finally, it checks if the original number is equal to the reversed number.
# The time complexity of this function is O(log n) because the number of digits in a number n is proportional to log(n).
# The space complexity is O(1) because we are using a constant amount of space for the rev variable.

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.isPalindrome(n))