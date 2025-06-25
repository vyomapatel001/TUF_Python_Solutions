def romanToInt(s:str)->int:
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    total = 0 # Initialize total to 0
    prev_value = 0 # Initialize previous value to 0
    # Iterate through the string in reverse order

    for ch in reversed(s):
        value=roman[ch] # Get the integer value of the Roman numeral character
        # If the current value is less than the previous value, subtract it from total
        if value<prev_value:
            total-=value
        else:
            total+=value
        prev_value=value # Update previous value to current value for next iteration
    return total


if __name__=="__main__":
    s= "III"
    print(romanToInt(s))

    s="LVIII"
    print(romanToInt(s))

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1), as we are using a fixed-size dictionary and a few variables.