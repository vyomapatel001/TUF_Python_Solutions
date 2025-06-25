class Solution:
    def getSingleElement(self, arr):
        """
        Find the single element in a list where every other element appears twice.
        :param arr: List[int] - A list containing integers where every element except one appears twice.
        :return: int - The single element that appears only once.
        """
        single_element = 0
        for num in arr:
            single_element ^= num
        return single_element
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), as we are using a constant amount of space.
# Example usage:
solution = Solution()
arr = [4, 1, 2, 1, 2]
result = solution.getSingleElement(arr)
print(result)  # Output: 4

# Second Approach:
class Solution:
     def getSingleElement(self, arr): 
         """
         Find the single element in a list where every other element appears twice using sorting.  
         :param arr: List[int] - A list containing integers where every element except one appears twice.
         :return: int - The single element that appears only once.
         """
         arr.sort()
         for i in range(0, len(arr) - 1, 2):
             if arr[i] != arr[i + 1]:
                 return arr[i]
         return arr[-1]  # If no pair is found, the last element is the single one.
# Time Complexity: O(n log n), where n is the length of the array due to sorting.
# Space Complexity: O(1), as we are using a constant amount of space.
# Example usage:
solution = Solution()
arr = [4, 1, 2, 1, 2]
result = solution.getSingleElement(arr)
print(result)  # Output: 4

# Third Approach:
class Solution:   
     def getSingleElement(self, arr):
         """
         Find the single element in a list where every other element appears twice using a set.
         :param arr: List[int] - A list containing integers where every element except one appears twice.
         :return: int - The single element that appears only once.
         """
         num_set = set()
         for num in arr:
             if num in num_set:
                 num_set.remove(num)
             else:
                 num_set.add(num)
         return num_set.pop() if num_set else None
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(n), as we are using a set to store elements.

# Example usage:
solution = Solution()
arr = [4, 1, 2, 1, 2]
result = solution.getSingleElement(arr)
print(result)  # Output: 4

# Fourth Approach:
class Solution:
    def getSingleElement(self, arr):
         """
         Find the single element in a list where every other element appears twice using a dictionary.
         :param arr: List[int] - A list containing integers where every element except one appears twice.
         :return: int - The single element that appears only once.
         """
         num_count = {}
         for num in arr:
             if num in num_count:
                 num_count[num] += 1
             else:
                 num_count[num] = 1
         for num, count in num_count.items():
             if count == 1:
                 return num
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(n), as we are using a dictionary to store the count of each element.