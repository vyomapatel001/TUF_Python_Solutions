class Solution:
    def isPrime(self, n):
        #your code goes here
        if n <= 1: # 0 and 1 are not prime numbers
            return False
        if n <=3: # 2 and 3 are prime numbers
            return True
        if n % 2 == 0 or n % 3 == 0: # Exclude multiples of 2 and 3
            return False
        i = 5 # Start checking from 5
        # Check for factors of the form 6k ± 1
        # where k is a positive integer
        while i * i <= n: # Check up to the square root of n
            # Check if n is divisible by i or i + 2
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
# Time Complexity: O(sqrt(n)) because we only check for factors up to the square root of n.
# Space Complexity: O(1) because we are using a constant amount of space for the variables.
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.isPrime(n))