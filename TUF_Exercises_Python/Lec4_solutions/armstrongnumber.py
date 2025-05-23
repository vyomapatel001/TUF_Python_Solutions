class Solution:
    def isArmstrong(self, n):
        #Count the number of digits in n
        num_digits = len(str(n))
        #Calculate the sum of the digits raised to the power of num_digits
        sum_of_powers = sum(int(digit) ** num_digits for digit in str(n))
        #Check if the sum of powers is equal to n
        return sum_of_powers == n
# Time Complexity: O(d) where d is the number of digits in n, because we need to iterate through each digit to calculate the sum of powers.
# Space Complexity: O(1) because we are using a constant amount of space for the variables.
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.isArmstrong(n))