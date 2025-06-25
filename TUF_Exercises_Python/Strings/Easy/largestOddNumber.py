def largestOddNumber(num:str)->str:
    for i in range(len(num)-1,-1,-1): #
        if int(num[i])%2==1:
            return num[:i+1]
    return ""

if __name__ == "__main__":
    num ="35427"
    print(largestOddNumber(num)) #Outputs "35427"

    num ="4206"
    print(largestOddNumber(num))

    num="52"
    print(largestOddNumber(num))

# Time Complexity: O(n), where n is the length of the string num.
# Space Complexity: O(1), as we are not using any additional data structures that grow with input size.
