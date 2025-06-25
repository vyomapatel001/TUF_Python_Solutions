class Solution:
    def unionoftwosortedarrays(self, arr1, arr2):
        """
        Find the union of two sorted arrays.
        :param arr1: List[int] - The first sorted array.
        :param arr2: List[int] - The second sorted array.
        :return: List[int] - A list containing the union of the two arrays with unique elements.
        """
        union_set = set(arr1) | set(arr2)
        union_list = sorted(union_set)
        return union_list
# Time Complexity: O(n + m), where n is the length of arr1 and m is the length of arr2.
# Space Complexity: O(n + m), as we are using a set to store unique elements from both arrays.
# Example usage:
solution = Solution()
arr1 = [1, 2, 4, 5]
arr2 = [2, 3, 5, 6]
result = solution.unionoftwosortedarrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Second Approach:
class Solution:
    def unionoftwosortedarrays(self, arr1, arr2):
        """
        Find the union of two sorted arrays using two pointers.
        :param arr1: List[int] - The first sorted array.
        :param arr2: List[int] - The second sorted array.
        :return: List[int] - A list containing the union of the two arrays with unique elements.
        """
        union_list = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if not union_list or union_list[-1] != arr1[i]:
                    union_list.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union_list or union_list[-1] != arr2[j]:
                    union_list.append(arr2[j])
                j += 1
            else:
                if not union_list or union_list[-1] != arr1[i]:
                    union_list.append(arr1[i])
                i += 1
                j += 1
        while i < len(arr1):
            if not union_list or union_list[-1] != arr1[i]:
                union_list.append(arr1[i])
            i += 1
        while j < len(arr2):
            if not union_list or union_list[-1] != arr2[j]:
                union_list.append(arr2[j])
            j += 1
        return union_list
# Time Complexity: O(n + m), where n is the length of arr1 and m is the length of arr2.
# Space Complexity: O(n + m), as we are using a list to store unique elements from both arrays.
# Example usage:
solution = Solution()  
arr1 = [1, 2, 4, 5]
arr2 = [2, 3, 5, 6]
result = solution.unionoftwosortedarrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]

#Third Approach:
class Solution:
    def unionoftwosortedarrays(self, arr1, arr2):
        """
        Find the union of two sorted arrays using a set to ensure uniqueness.
        :param arr1: List[int] - The first sorted array.
        :param arr2: List[int] - The second sorted array.
        :return: List[int] - A list containing the union of the two arrays with unique elements.
        """
        union_list = []
        seen = set()
        for num in arr1 + arr2:
            if num not in seen:
                seen.add(num)
                union_list.append(num)
        union_list.sort()
        return union_list
# Time Complexity: O(n + m + k log k), where n is the length of arr1, m is the length of arr2, and k is the number of unique elements.
# Space Complexity: O(n + m), as we are using a set to store unique elements from both arrays.

# Example usage:
solution = Solution()
arr1 = [1, 2, 4, 5]
arr2 = [2, 3, 5, 6]
result = solution.unionoftwosortedarrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
# This approach combines both arrays, checks for uniqueness using a set, and then sorts the result.