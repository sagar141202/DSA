# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it's impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range `[1, 500]`. For example, given the string "aaab", the function should return an empty string because it's impossible to reorganize the string. However, given the string "aab", the function should return "aba".

## Approach
The approach to solve this problem is to use a max heap to store the frequency of each character. We then pop the two most frequent characters from the heap and append them to the result string. This process is repeated until the heap is empty or only one character is left in the heap.

## Complexity
- Time: O(N log N)
- Space: O(N)

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

        // Push the characters into a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto& pair : freq) {
            maxHeap.push({pair.second, pair.first});
        }

        // Initialize the result string
        string result;
        while (!maxHeap.empty()) {
            // Pop the two most frequent characters from the heap
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
Input: "aaab"
Output: ""
Input: "aab"
Output: "aba"
```

## Key Takeaways
- Use a max heap to store the frequency of each character.
- Pop the two most frequent characters from the heap and append them to the result string.
- Handle the case where only one character is left in the heap.