def count_freq_brute_force(arr, queries):
    """
    Count the frequency of each character in the string s using brute force.
    """
    result = []
    for q in queries:
        count = 0
        for num in arr:
            if num == q:
                count += 1
        result.append(count)
    return result
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2]
    queries = [1, 3, 4, 2, 10]
    result = count_freq_brute_force(arr, queries)
    print("Frequencies:", result)

# This function counts the frequency of each number in the array using a brute force approach.
# Time Complexity: O(n * m) - where n is the length of arr and m is the length of queries, as it checks each element in arr for each query.
# Space Complexity: O(m) - for storing the results of the queries.
