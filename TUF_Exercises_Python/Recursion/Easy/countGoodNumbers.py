'''A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 10**9 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
'''
MOD = 10**9+7

def mod_pow(base, exp, mod): # Fast exponentiation
    if exp == 0:
        return 1
    half = mod_pow(base, exp//2, mod) # Recursive call
    half = (half*half)%mod # Square the result if exp is even, why? Because (a^b)^2 = a^(2*b)
    if exp%2==1: # If exp is odd, then multiply by base once more why? Because a^(2*b+1) = a^(2*b) * a
        half = (half*base)%mod
    return half
def countGoodNumbers(n:int)->int:
    even_positions = (n + 1) // 2  # Count of even indices
    odd_positions = n // 2         # Count of odd indices
    return (mod_pow(5, even_positions, MOD)* mod_pow(4,odd_positions,MOD))

if __name__ =="__main__":
    n=5
    print(countGoodNumbers(n))
    n=4
    print(countGoodNumbers(n))
    n=1
    print(countGoodNumbers(n))

#Time Complexity: O(log n) due to the fast exponentiation.
#Space Complexity: O(log n) due to the recursion stack in the fast exponentiation function.
# The function mod_pow computes the power of a number modulo a given value efficiently using the method of exponentiation by squaring.

