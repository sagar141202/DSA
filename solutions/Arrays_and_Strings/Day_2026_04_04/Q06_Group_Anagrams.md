# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams. For example, given the input `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat","tea","ate"],["tan","nat"],["bat"]]`. The order of the sublists and the order of the strings within each sublist do not matter.

## Approach
The approach to solve this problem is to use a hashmap where the sorted version of each string is the key and the value is a list of strings that are anagrams of the key. We iterate over each string in the input array, sort its characters, and use the sorted string as a key in the hashmap. If the key is already present, we append the current string to its value list; otherwise, we create a new key-value pair.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> map;
    for (string str : strs) {
        string sortedStr = str;
        sort(sortedStr.begin(), sortedStr.end());
        map[sortedStr].push_back(str);
    }
    vector<vector<string>> result;
    for (auto& pair : map) {
        result.push_back(pair.second);
    }
    return result;
}

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = groupAnagrams(strs);
    for (vector<string> group : result) {
        for (string str : group) {
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
```

## Key Takeaways
- Use a hashmap to group anagrams together based on their sorted characters.
- The time complexity is dominated by the sorting operation for each string, resulting in O(NMlogM) time complexity, where N is the number of strings and M is the maximum length of a string.
- The space complexity is O(NM) due to the storage of the input strings in the hashmap.