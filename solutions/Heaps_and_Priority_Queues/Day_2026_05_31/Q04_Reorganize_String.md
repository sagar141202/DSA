# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 100. For example, given the string "aab", the reorganized string is "aba". However, given the string "aaab", it is not possible to reorganize the string.

## Approach
The approach is to use a max heap to store the frequency of each character. Then, we pop the two characters with the highest frequency from the heap and add them to the result string. We push the characters back into the heap if their frequency is greater than 0. This process is repeated until the heap is empty or we cannot add a character to the result string without having two adjacent characters being the same.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        // Create a frequency map
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        // Create a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }
        
        string result;
        while (!maxHeap.empty()) {
            // Get the two characters with the highest frequency
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (result.size() > 0 && result.back() == first.second) {
                if (maxHeap.empty()) {
                    return "";
                }
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();
                result.push_back(second.second);
                if (second.first > 1) {
                    maxHeap.push({second.first - 1, second.second});
                }
                maxHeap.push(first);
            } else {
                result.push_back(first.second);
                if (first.first > 1) {
                    maxHeap.push({first.first - 1, first.second});
                }
            }
        }
        return result;
    }
};
```

## Test Cases
```
Input: "aab"
Output: "aba"
Input: "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character.
- Pop the two characters with the highest frequency from the heap and add them to the result string.
- Push the characters back into the heap if their frequency is greater than 0.