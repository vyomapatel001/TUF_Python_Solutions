def char_frequency_lowercase(s, queries):
    hash_arr = [0] * 26 #26 lowercase letters so filled with zeros
    for char in s:
        hash_arr[ord(char) - ord('a')] += 1
    return [hash_arr[ord(q) - ord('a')] for q in queries]



if __name__ == "__main__":
    # Example
    s = "abcdabefc"
    queries = ['a', 'c', 'z']
    print(char_frequency_lowercase(s, queries))  # Output: [2, 2, 0]

# This function counts the frequency of each lowercase character in the string s using a hash array.
# Time Complexity: O(n + m) - where n is the length of s and m is the length of queries, as it processes each character in s once and then each query once.
# Space Complexity: O(1) - the hash array has a fixed size of 26, regardless of the input size.
# Note: This function assumes that the input string s contains only lowercase letters and that the queries are also lowercase letters.