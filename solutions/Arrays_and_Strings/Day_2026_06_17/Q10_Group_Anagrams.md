# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters and no empty strings. The output should be a list of lists, where each sublist contains the anagrams from the input array. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`.

## Approach
The approach to solve this problem is to use a hashmap to store the sorted version of each string as the key and the original string as the value. This way, all anagrams will have the same key and can be grouped together. The algorithm iterates over the input array, sorts each string, and uses the sorted string as the key in the hashmap.

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
        
        // Iterate over the input array
        for (string str : strs) {
            // Sort the characters in the string
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            
            // Use the sorted string as the key in the hashmap
            anagrams[sortedStr].push_back(str);
        }
        
        // Convert the hashmap values to a list of lists
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
- Use a hashmap to group the anagrams together based on the sorted version of each string.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.
- The space complexity is O(NM) to store the hashmap and the result.