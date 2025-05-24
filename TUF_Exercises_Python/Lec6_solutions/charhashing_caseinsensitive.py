def char_frequency_all(s, queries):
    hash_arr = [0] * 256
    for char in s:
        hash_arr[ord(char)] += 1
    return [hash_arr[ord(q)] for q in queries]

if __name__ == "__main__":
    # Example
    s = "abCDabEfC"
    queries = ['a', 'C', 'z']
    print(char_frequency_all(s, queries))  # Output: [2, 2, 0]
    
# This function counts the frequency of each character in the string s using a hash array.
# Time Complexity: O(n + m) - where n is the length of s and m is the length of queries, as it processes each character in s once and then each query once.
# Space Complexity: O(1) - the hash array has a fixed size of 256, regardless of the input size.
# Note: This function handles all ASCII characters, including uppercase and lowercase letters, digits, punctuation, and control characters.