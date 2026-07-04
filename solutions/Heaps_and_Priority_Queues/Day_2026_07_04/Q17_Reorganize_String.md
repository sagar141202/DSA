# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and has a length of at most 10^5. For example, given the string "aab", the function should return "aba". If the string "aaab" is given, the function should return an empty string because it is not possible to reorganize the string.

## Approach
We can use a max heap to store the frequency of each character in the string. We then pop the two characters with the highest frequency from the heap, add them to the result string, and push them back into the heap with their frequencies decremented. This process is repeated until the heap is empty or it is not possible to reorganize the string.

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
        // Create a frequency map of characters in the string
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap to store the frequency of each character
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        // Initialize the result string
        string result;
        while (!maxHeap.empty()) {
            // Pop the two characters with the highest frequency from the heap
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
- Use a max heap to store the frequency of each character in the string.
- Pop the two characters with the highest frequency from the heap and add them to the result string.
- If it is not possible to reorganize the string, return an empty string.