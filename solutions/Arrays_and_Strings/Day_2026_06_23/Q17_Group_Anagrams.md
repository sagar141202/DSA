# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters and no empty strings. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`.

## Approach
The approach is to use a hashmap to store the sorted version of each string as the key and the original string as the value. This way, all anagrams will have the same key and can be grouped together. The algorithm iterates over the input array, sorts each string, and adds it to the hashmap.

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
        for (const string& str : strs) {
            // Create a copy of the string to sort
            string sortedStr = str;
            
            // Sort the characters in the string
            sort(sortedStr.begin(), sortedStr.end());
            
            // Add the original string to the hashmap
            anagrams[sortedStr].push_back(str);
        }
        
        // Convert the hashmap values to a vector of vectors
        vector<vector<string>> result;
        for (const auto& pair : anagrams) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = solution.groupAnagrams(strs);
    
    // Print the result
    for (const auto& group : result) {
        for (const auto& str : group) {
            cout << str << " ";
        }
        cout << endl;
    }
    
    return 0;
}
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
- The time complexity is O(NMlogM) due to the sorting operation for each string.
- The space complexity is O(NM) to store the input strings and their sorted versions in the hashmap.