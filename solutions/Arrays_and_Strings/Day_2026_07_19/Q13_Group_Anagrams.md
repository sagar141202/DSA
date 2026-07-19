# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`. The order of the sublists and the order of the strings within the sublists do not matter.

## Approach
The approach to solve this problem is to use a hashmap where the sorted version of each string is used as the key and the value is a list of strings that are anagrams of the key. We iterate over the input array, sort each string, and use the sorted string as the key in the hashmap.

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
            // Sort the characters in the string
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            
            // Use the sorted string as the key in the hashmap
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

int main() {
    Solution solution;
    vector<string> input = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = solution.groupAnagrams(input);
    
    // Print the result
    for (const auto& sublist : result) {
        cout << "[";
        for (size_t i = 0; i < sublist.size(); ++i) {
            cout << "\"" << sublist[i] << "\"";
            if (i < sublist.size() - 1) {
                cout << ", ";
            }
        }
        cout << "], ";
    }
    
    return 0;
}
```

## Test Cases
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Input: [""]
Output: [[""]]
Input: ["a"]
Output: [["a"]]
```

## Key Takeaways
- Use a hashmap to efficiently group the anagrams together.
- Sort the characters in each string to create a unique key for the hashmap.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.