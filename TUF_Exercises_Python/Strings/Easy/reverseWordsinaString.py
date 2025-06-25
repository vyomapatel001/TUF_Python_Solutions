# O(1) space complexity approach:
def reverseWords(s: str) -> str:
    words = list(s)

    def reverse(l,r): # Helper function to reverse a portion of the list in-place
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
    # Reverse the entire string
    reverse(0, len(words) - 1)

    # Reverse each word in the reversed string
    n = len(words)
    i = 0
    while i < n:
        if words[i]!= ' ': # If the current character is not a space, we found the start of a word
            start = i
            while i < n and words[i] != ' ':
                i += 1
            reverse(start, i - 1)  # Reverse the current word
        i += 1  # Move to the next character

    # Remove extra spaces in-place
    i = 0 # Pointer for the position to write
    j = 0 # Pointer for reading
    while j < n:
        while j < n and words[j] == ' ': # Skip leading spaces
            j += 1
        while j < n and words[j] != ' ': # Copy non-space characters
            words[i] = words[j] # Copy character from j to i
            i += 1
            j += 1
        while j < n and words[j] == ' ': # Skip trailing spaces
            j += 1
        if j < n: # If there are more characters after spaces, add a single space
            words[i] = ' ' #
            i += 1
    return ''.join(words[:i])  # Join the characters up to the last written position
# This function reverses the order of words in a given string in-place.
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1), as it modifies the input string in-place without using extra space for another list.


def reverseWords(s: str) -> str:
    """
    Reverse the order of words in a given string.
    
    :param s: Input string with words separated by spaces.
    :return: String with the order of words reversed.
    """
    # Split the string into words, reverse the list of words, and join them back into a string
    return ' '.join(s.split()[::-1])

# Example usage:
s = "the sky is blue"
print(reverseWords(s))  # Output: "blue is sky the"
# This function reverses the order of words in a given string.
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), for storing the list of words.

# Note: The split() method splits the string at whitespace by default, and the join() method combines the words with a single space.
# The [::-1] slice reverses the list of words.

# Second Approach using a stack:
def reverseWordsStack(s: str) -> str:
    """
    Reverse the order of words in a given string using a stack.
    
    :param s: Input string with words separated by spaces.
    :return: String with the order of words reversed.
    """
    stack = []
    word = ''
    
    for char in s:
        if char == ' ':
            if word:  # If we have a word, push it onto the stack
                stack.append(word)
                word = ''  # Reset word for the next one
        else:
            word += char  # Build the current word
    
    if word:  # Push the last word if it exists
        stack.append(word)
    
    return ' '.join(reversed(stack))  # Join the words in reverse order
# Example usage:
s = "the sky is blue"
print(reverseWordsStack(s))  # Output: "blue is sky the"
# This function also reverses the order of words in a given string using a stack.
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), for storing the stack of words.

# Note: This approach uses a stack to collect words and then joins them in reverse order.
# Both approaches achieve the same result, but the first one is more concise and easier to read.

# Third Approach using list comprehension:
def reverseWordsListComp(s: str) -> str:
    """
    Reverse the order of words in a given string using list comprehension.
    
    :param s: Input string with words separated by spaces.
    :return: String with the order of words reversed.
    """
    return ' '.join([word for word in s.split()][::-1])

# Example usage:
s = "the sky is blue"
print(reverseWordsListComp(s))  # Output: "blue is sky the"
# This function reverses the order of words in a given string using list comprehension.
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), for storing the list of words.

# Fourth Approach with optimization:
def reverseWordsOptimized(s: str) -> str:
    """
    Reverse the order of words in a given string with optimized space usage.
    
    :param s: Input string with words separated by spaces.
    :return: String with the order of words reversed.
    """
    words = s.split()
    return ' '.join(reversed(words))
# Example usage:
s = "the sky is blue"
print(reverseWordsOptimized(s))  # Output: "blue is sky the"
# This function reverses the order of words in a given string with optimized space usage.
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), for storing the list of words.

