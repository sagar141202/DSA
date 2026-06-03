# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within each sublist does not matter.

## Approach
The approach to solve this problem is to use an unordered map where the key is the sorted version of the string and the value is a list of strings that are anagrams of the key. We iterate over each string in the input array, sort its characters, and use the sorted string as a key in the map. If the key is already present, we append the string to the list of values. If not, we create a new key-value pair.

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
        // Create an unordered map to store the anagrams
        unordered_map<string, vector<string>> anagrams;
        
        // Iterate over each string in the input array
        for (string str : strs) {
            // Sort the characters of the string
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            
            // Use the sorted string as a key in the map
            anagrams[sortedStr].push_back(str);
        }
        
        // Convert the map values to a vector of vectors
        vector<vector<string>> result;
        for (auto& pair : anagrams) {
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
Input: [""]
Output: [[""]]
Input: ["a"]
Output: [["a"]]
```

## Key Takeaways
- Use an unordered map to store the anagrams, where the key is the sorted version of the string.
- Sort the characters of each string to create a unique key for anagrams.
- Iterate over the map values to convert the result to a vector of vectors.