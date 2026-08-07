# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters and no empty strings. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the groups and the order of the strings within each group do not matter.

## Approach
The algorithm uses a hashmap to store the sorted version of each string as the key and a list of anagrams as the value. It iterates over each string in the input array, sorts its characters, and uses this sorted string as a key in the hashmap. If the key is already present, it appends the current string to the list of values; otherwise, it creates a new key-value pair.

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
        for (const string& word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());
            anagrams[sortedWord].push_back(word);
        }
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
    for (const auto& group : result) {
        for (const auto& word : group) {
            cout << word << " ";
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
```

## Key Takeaways
- Use a hashmap to efficiently group anagrams together based on their sorted characters.
- The time complexity is dominated by the sorting operation for each string, resulting in O(NMlogM) time complexity, where N is the number of strings and M is the maximum length of a string.
- The space complexity is O(NM) due to the storage of all characters from the input strings in the hashmap.