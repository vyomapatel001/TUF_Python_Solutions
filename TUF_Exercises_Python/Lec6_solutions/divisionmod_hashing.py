def division_hashing(arr, query, mod):
    hash_table = [[] for _ in range(mod)]
    for num in arr:
        hash_table[num % mod].append(num)
    
    result = []
    for q in query:
        bucket = hash_table[q % mod]
        result.append(bucket.count(q))
    return result

if __name__ == "__main__": 
    # Example usage
    arr = [2, 5, 16, 28, 139, 38, 48, 28, 18]
    queries = [28, 38, 18, 8]
    print(division_hashing(arr, queries, 10))  # Output: [2, 1, 1, 0]

# This function counts the frequency of each number in the array using division hashing.
# Time Complexity: O(n + m) - where n is the length of arr and m is the length of query, as it processes each element in arr once and then each query once.
# Space Complexity: O(n) - for storing the hash table, which has a size of mod.
# Note: The hash table uses the modulo operation to determine the bucket for each number, which allows for efficient frequency counting.
