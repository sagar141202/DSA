# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains all the anagrams from the input array. For example, if the input is `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within each sublist do not matter.

## Approach
The approach is to use an unordered map to store the sorted characters of each string as the key and a list of strings that are anagrams of each other as the value. We iterate over the input array, sort the characters of each string, and use the sorted characters as the key in the map. If the key is already in the map, we append the current string to the list of values. If the key is not in the map, we create a new entry with the sorted characters as the key and a list containing the current string as the value.

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
        unordered_map<string, vector<string>> map;
        for (const string& str : strs) {
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            map[sortedStr].push_back(str);
        }
        vector<vector<string>> result;
        for (const auto& pair : map) {
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
- We use an unordered map to store the sorted characters of each string as the key and a list of strings that are anagrams of each other as the value.
- We iterate over the input array and sort the characters of each string to use as the key in the map.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.