def count_frequency_dict(arr, query):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return [freq.get(q, 0) for q in query]

if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2]
    queries = [1, 3, 4, 2, 10]
    result = count_frequency_dict(arr, queries)
    print("Frequencies:", result)

# This function counts the frequency of each number in the array using a dictionary.
# Time Complexity: O(n + m) - where n is the length of arr and m is the length of query, as it processes each element in arr once and then each query once.
# Space Complexity: O(n) - for storing the frequency counts in the dictionary.
# Note: The dictionary approach is generally more efficient than the brute force method, especially for larger datasets.