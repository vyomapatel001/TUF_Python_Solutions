from collections import Counter
def sortbyfrequency(s:str)->str:
    frequency = Counter(s)
    sorted_char = sorted(frequency.items(), key= lambda x: x[1], reverse=True)
    return ''.join(char*freq for char, freq in sorted_char)

if __name__=="__main__":
    s="tree"
    print(sortbyfrequency(s))

#Time Complexity: O(n log n), where n is the length of the string s due to sorting.
#Space Complexity: O(n), where n is the number of unique characters in the string s


# Second approach using heapq
from collections import Counter
import heapq
def sortbyfrequsingheap(s:str)->str:
    counts = Counter(s)
    max_heap = [(-freq, char) for char, freq in counts.items()]
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char*(-freq))

    return ''.join(result)


if __name__=="__main__":
    s="fleet"
    print(sortbyfrequsingheap(s))

#Time Complexity: O(n log k), where n is the length of the string s and k is the number of unique characters.
#Space Complexity: O(n), where n is the number of unique characters in the string s