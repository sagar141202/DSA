# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within each sublist do not matter.

## Approach
The approach is to use a hashmap to store the sorted version of each string as the key and a list of anagrams as the value. We iterate over each string in the input array, sort its characters, and use the sorted string as a key in the hashmap. If the key already exists, we append the current string to the list of values. If not, we create a new key-value pair.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Create a hashmap to store the anagrams
        unordered_map<string, vector<string>> anagrams;
        
        // Iterate over each string in the input array
        for (const string& str : strs) {
            // Create a copy of the string to sort
            string sortedStr = str;
            
            // Sort the characters in the string
            sort(sortedStr.begin(), sortedStr.end());
            
            // Use the sorted string as a key in the hashmap
            anagrams[sortedStr].push_back(str);
        }
        
        // Convert the hashmap values to a list of lists
        vector<vector<string>> result;
        for (const auto& pair : anagrams) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

## Key Takeaways
- Use a hashmap to store the anagrams with the sorted string as the key.
- Sort the characters in each string to create a unique key.
- The time complexity is O(NMlogM) due to the sorting operation, where N is the number of strings and M is the maximum length of a string.