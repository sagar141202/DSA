# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams from the input array. For example, if the input is `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`. The order of the sublists and the order of the strings within the sublists do not matter.

## Approach
The approach to solve this problem is to use a hashmap where the sorted version of each string is the key and the value is a list of all strings that are anagrams of the key. We iterate over each string in the input array, sort its characters, and use the sorted string as the key in the hashmap. If the key is already present, we append the current string to its value list; otherwise, we create a new key-value pair.

## Complexity
- Time: O(NMlogM), where N is the number of strings and M is the maximum length of a string, due to the sorting operation for each string.
- Space: O(NM), for storing the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = groupAnagrams(strs);
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
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Input: [""]
Output: [[""]]
Input: ["a"]
Output: [["a"]]
```

## Key Takeaways
- Using a hashmap to group anagrams based on their sorted characters is an efficient approach.
- Sorting each string to create a unique key for anagrams has a time complexity of O(MlogM) per string.
- The overall space complexity is determined by the storage needed for the result, which is O(NM) in the worst case.