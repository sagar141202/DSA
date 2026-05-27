# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, "eat" and "tea" are anagrams, while "eat" and "tan" are not. The input array will contain at least one string, and all strings will only contain lowercase alphabets. The output should be a list of lists, where each sublist contains strings that are anagrams of each other.

## Approach
The algorithm uses a hashmap to store the sorted version of each string as the key and a list of anagrams as the value. It iterates over the input array, sorts each string, and adds it to the corresponding list in the hashmap. Finally, it returns the values in the hashmap as the result. The sorting operation takes O(n log n) time, and the overall time complexity is O(NM log M), where N is the number of strings and M is the maximum length of a string.

## Complexity
- Time: O(NM log M)
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
        for (const string& str : strs) {
            // Sort the characters in the string
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            
            // Add the string to the corresponding list in the hashmap
            anagrams[sortedStr].push_back(str);
        }
        
        // Return the values in the hashmap as the result
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
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## Key Takeaways
- Use a hashmap to store the sorted version of each string as the key and a list of anagrams as the value.
- Sort each string using the `sort` function from the C++ Standard Template Library.
- Iterate over the input array and add each string to the corresponding list in the hashmap.
- Return the values in the hashmap as the result, which represents the groups of anagrams.