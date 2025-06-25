def longestCommonPrefix(s:str)->str:
    if not s: # Check if the list is empty
        return "" # Return empty string if no strings are present
    for i in range(len(s[0])): # Iterate through the characters of the first string
        for word in s[1:]: # Compare with the rest of the strings
            if s[0][i]!=word[i] or i>=len(word): # If characters don't match or index exceeds length of word
                return s[0][:i] # Return the common prefix found so far
    # If we reach here, it means the first string is a common prefix for all strings
    return s[0]

if __name__=="__main__":
    s=["flower", "flow", "flock"]
    print(longestCommonPrefix(s))

    s=["dog", "racecar", "car"]
    print(longestCommonPrefix(s))  # Outputs ""

# Time Complexity: O(n*m), where n is the number of strings and m is the length of the shortest string.
# Space Complexity: O(1), as we are not using any additional data structures that grow with input size.


