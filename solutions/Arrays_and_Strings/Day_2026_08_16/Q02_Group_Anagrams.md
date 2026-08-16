# Group Anagrams

## Problem Statement
Given an array of strings, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The input array will contain only lowercase English letters. The output should be a list of lists, where each sublist contains the anagrams from the input array. For example, if the input is ["eat", "tea", "tan", "ate", "nat", "bat"], the output should be [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]. The order of the sublists and the order of the strings within each sublist do not matter.

## Approach
The algorithm uses a hashmap to store the sorted characters of each string as the key and a list of anagrams as the value. It iterates over each string in the input array, sorts its characters, and uses the sorted characters as the key in the hashmap. If the key already exists, it appends the string to the list of values; otherwise, it creates a new key-value pair.

## Complexity
- Time: O(NMlogM)
- Space: O(NM)

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
- Use a hashmap to store the anagrams, with the sorted characters as the key.
- Sort the characters of each string to create the key for the hashmap.
- The time complexity is O(NMlogM) due to the sorting of each string, where N is the number of strings and M is the maximum length of a string.