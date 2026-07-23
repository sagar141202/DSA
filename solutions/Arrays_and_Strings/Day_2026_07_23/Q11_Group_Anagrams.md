# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams from the input array. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within each sublist do not matter.

## Approach
The approach is to use a hashmap to store the sorted version of each string as the key and the original string as the value. This way, anagrams will have the same key and can be grouped together. The algorithm iterates over each string in the input array, sorts the characters in the string, and uses the sorted string as a key in the hashmap.

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
        
        // Create a result vector to store the grouped anagrams
        vector<vector<string>> result;
        
        // Iterate over each key-value pair in the hashmap
        for (const auto& pair : anagrams) {
            // Add the value (a vector of anagrams) to the result vector
            result.push_back(pair.second);
        }
        
        // Return the result vector
        return result;
    }
};
```

## Test Cases
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Input: [""]
Output: [[""]]
Input: ["a"]
Output: [["a"]]
```

## Key Takeaways
- Use a hashmap to group anagrams together based on their sorted characters.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.
- The space complexity is O(NM) to store the hashmap and the result vector.