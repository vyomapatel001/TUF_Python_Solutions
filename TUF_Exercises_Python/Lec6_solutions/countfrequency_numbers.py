def count_freq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for key, value in freq.items():
        print(key,value)  # Print the key and value of the freq dictionary

if __name__ == "__main__":
    # Example usage
    arr = [10,5,10,15,10,5]
    freq_dict = count_freq(arr)

#This function counts the frequency of each number in the array using a dictionary.
# Time Complexity: O(n) - where n is the length of arr, as it processes each element in arr once.
# Space Complexity: O(n) - for storing the frequency counts in the dictionary.
# Note: The dictionary approach is efficient for counting frequencies, especially for larger datasets.