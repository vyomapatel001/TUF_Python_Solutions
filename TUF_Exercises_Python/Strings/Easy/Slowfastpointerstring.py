#Slow and fast pointer string 
def reverseWords(s:str) -> str:
    chars = list(s)
    n = len(chars)

    def reverse(l:int, r:int) -> None:
        while l<r:
            chars[l], chars[r] = chars[r], chars[l]
            l+=1
            r-=1
    
    #Removing extra space in-place
    slow = 0
    fast = 0
    while fast < n:
        while fast < n and chars[fast] == ' ':
            fast+=1
        if fast >=n:
            break
        #Adding spaces in between words if needed
        if slow!=0:
            chars[slow] = ' '
            slow+=1
        
        #Copy the word
        while fast < n and chars[fast]!= ' ':
            chars[slow]=chars[fast]
            slow+=1
            fast+=1

    #Trim to new size
    chars = chars[:slow]

    #Reverse entire string
    reverse(0, len(chars)-1)

    #Reverse each word
    start = 0
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == ' ':
            reverse(start, i - 1)
            start = i + 1
    
    return ''.join(chars)

if __name__ == "__main__":
    s= "  the sky is blue  "
    print(reverseWords(s))
