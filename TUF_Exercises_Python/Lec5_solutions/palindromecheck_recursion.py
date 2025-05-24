class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        def is_palindrome(s, start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return is_palindrome(s, start + 1, end - 1)
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        return is_palindrome(s, 0, len(s) - 1)

if __name__ == "__main__":
    s = input("Enter a string: ")
    solution = Solution()
    if solution.palindromeCheck(s):
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

# This function checks if a given string is a palindrome using recursion.
# Time Complexity: O(n) - where n is the length of the string, as it processes each character once.
# Space Complexity: O(n) - due to the recursive call stack.
