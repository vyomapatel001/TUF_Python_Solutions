#First Approach
'''class Solution:
    def divisors(self, n):
        result = []
        for i in range(1,n+1):
            if n%i==0:
                result.append(i)
        return result'''
# The above code is a brute-force approach to find the divisors of a number n.
# Time Complexity: O(n) because we are iterating through all numbers from 1 to n to find the divisors.
# Space Complexity: O(n) because in the worst case, we may store all divisors of n in the result list.


#Second Approach
class Solution:
    def divisors(self, n):
        result = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                result.append(i)
                if i != n // i:  # Avoid adding the square root twice
                    result.append(n // i)
        return sorted(result)
    
# Time Complexity: O(sqrt(n)) because we only iterate up to the square root of n to find divisors.
# Space Complexity: O(sqrt(n)) in the worst case, we may store all divisors of n in the result list.
# The second approach is more efficient for larger values of n, as it reduces the number of iterations significantly.
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.divisors(n))