# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within the sublists do not matter.

## Approach
The approach is to use a hashmap to store the sorted characters of each string as the key and the original string as the value. By sorting the characters of each string, anagrams will have the same key, allowing them to be grouped together. The algorithm iterates through the input array, sorts the characters of each string, and adds it to the hashmap. Finally, it constructs the output list by grouping the values in the hashmap.

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
        unordered_map<string, vector<string>> anagrams;
        for (const string& str : strs) {
            string sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            anagrams[sorted_str].push_back(str);
        }
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
Input: [""]
Output: [[""]]
Input: ["a"]
Output: [["a"]]
```

## Key Takeaways
- Use a hashmap to group anagrams together based on their sorted characters.
- Sort the characters of each string to create a unique key for anagrams.
- Construct the output list by grouping the values in the hashmap.