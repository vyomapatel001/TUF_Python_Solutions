def count_frequency_hashing(arr, query, max_val):
    hash_arr = [0] * (max_val) # Initialize a hash array with zeros of size max_val + 1
    for num in arr:
        hash_arr[num] += 1
    return [hash_arr[q] if q <= max_val else 0 for q in query]

# Example
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2]
    queries = [1, 3, 4, 2, 10]
#max value calcation formula:
# max_val = max(arr + queries)  # This is not needed if we know the max value beforehand
    print(count_frequency_hashing(arr, queries, 13))  # Output: [2, 1, 0, 2, 0]