def removeOuterParentheses(S: str) -> str:
    count = 0
    result = []
    
    for char in S:
        if char == '(':
            if count > 0: # Only append if not the outermost '('
                result.append(char)
            count += 1 # Increment count for '('
        elif char == ')':
            count -= 1 # Decrement count for ')'
            if count > 0: # Only append if not the outermost ')'
                result.append(char)
    
    return ''.join(result)

# Example usage:
S = "(()())(())"
print(removeOuterParentheses(S))  # Output: "()()()"

# This function removes the outermost parentheses from a given string of parentheses.
# Time Complexity: O(n), where n is the length of the string S.
# Space Complexity: O(n), for storing the result in a list.