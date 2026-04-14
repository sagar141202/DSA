# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within each sublist does not matter.

## Approach
The approach is to use a hashmap where the sorted version of each string is the key and the value is a list of anagrams. We iterate through each string, sort its characters, and use the sorted string as the key in the hashmap. If the key exists, we append the original string to the list of values. If the key does not exist, we create a new entry in the hashmap with the sorted string as the key and a list containing the original string as the value.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // Create a hashmap to store the anagrams
    unordered_map<string, vector<string>> anagrams;
    
    // Iterate through each string in the input array
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

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = groupAnagrams(strs);
    
    // Print the result
    for (vector<string> group : result) {
        cout << "[";
        for (int i = 0; i < group.size(); i++) {
            cout << "\"" << group[i] << "\"";
            if (i < group.size() - 1) {
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
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
```

## Key Takeaways
- Use a hashmap to group the anagrams together based on the sorted version of each string.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.
- The space complexity is O(NM) to store the anagrams in the hashmap.