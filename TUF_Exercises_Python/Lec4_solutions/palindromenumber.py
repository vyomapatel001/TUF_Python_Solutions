class Solution:
    def isPalindrome(self, n):
        # Convert the number to a string
        str_n = str(n)
        # Check if the string is equal to its reverse
        return str_n == str_n[::-1]
    
# The function isPalindrome checks if a given integer n is a palindrome.
# A palindrome is a number that reads the same backward as forward.
# The function converts the number to a string and checks if the string is equal to its reverse.
# The time complexity of this function is O(d), where d is the number of digits in the number n, because we need to create a string representation of n and check for equality.
# The space complexity is O(d) because we are storing the string representation of n.

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.isPalindrome(n))
    