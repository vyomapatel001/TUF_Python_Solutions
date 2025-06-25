def max_depth_parantheses(s:str)->int:
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == '(':
            current_depth+=1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth-=1
    return max_depth


if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"
    print(max_depth_parantheses(s))

    s = "()(())((()()))"
    print(max_depth_parantheses(s))

#Time Complexity: O(n)
#Space Complexity: O(1)