# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams from the input array. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`.

## Approach
The algorithm uses an unordered map to store the sorted version of each string as the key and a list of anagrams as the value. This approach works by iterating over each string in the input array, sorting its characters, and using the sorted string as a key in the map. The time complexity is optimized by using a hashmap for storing the anagrams.

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
        for (const string& s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            anagrams[sorted_s].push_back(s);
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
```

## Key Takeaways
- Use an unordered map to efficiently store and retrieve anagrams.
- Sort the characters of each string to create a unique key for anagrams.
- Iterate over the input array and the map to construct the result.