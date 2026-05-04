# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`. The order of the sublists and the order of the strings within each sublist do not matter.

## Approach
The algorithm uses an unordered map to group the anagrams together. It sorts each string and uses the sorted string as the key in the map. The value associated with each key is a list of strings that are anagrams of each other. This approach works because anagrams will have the same characters when sorted.

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
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            anagrams[sortedStr].push_back(str);
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
        cout << "{";
        for (const auto& str : group) {
            cout << str << ", ";
        }
        cout << "}" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

## Key Takeaways
- Use an unordered map to group the anagrams together.
- Sort each string and use the sorted string as the key in the map.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.