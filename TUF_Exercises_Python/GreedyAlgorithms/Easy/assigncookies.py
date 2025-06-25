def findContentChildren(g: list, s: list) -> int:
    g.sort() # Sort the greed factor of children
    s.sort() # Sort the size of cookies
    child_i = 0 # Index for children
    cookies_i = 0 # Index for cookies   

    while child_i<len(g) and cookies_i<len(s): # While there are children and cookies left
        # If the current cookie can satisfy the current child
        if g[child_i] <= s[cookies_i]: # If the current cookie can satisfy the current child
            child_i += 1 # Move to the next child
        # Move to the next cookie regardless of whether the current child was satisfied
        cookies_i += 1
    # Return the number of satisfied children
    return child_i

# Example usage:
if __name__ == "__main__":
    g = [1, 2, 3]  # Greed factors of children
    s = [1, 1]     # Sizes of cookies
    print(findContentChildren(g, s))  # Output: 1
    g = [1, 2]
    s = [1, 2, 3]
    print(findContentChildren(g, s))  # Output: 2
    g = [10, 9, 8]
    s = [5, 6, 7]
    print(findContentChildren(g, s))  # Output: 0
# tIME COMPLEXITY: O(nlogn + mlogm) where n is the number of children and m is the number of cookies
# SPACE COMPLEXITY: O(1) since we are sorting in place and not using

