# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 100.

## Approach
The approach to solve this problem is to use a max heap to store the frequency of each character. We then pop the two characters with the highest frequency from the heap, add them to the result string, and push them back into the heap with decreased frequency.

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
        // Count the frequency of each character
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
            if (maxHeap.empty()) {
                // If there is only one character left, return an empty string if its frequency is more than 1
                if (first.first > 1) {
                    return "";
                } else {
                    result += first.second;
                }
                break;
            }
            pair<int, char> second = maxHeap.top();
            maxHeap.pop();

            // Add the characters to the result string
            result += first.second;
            result += second.second;

            // Push the characters back into the heap with decreased frequency
            if (first.first > 1) {
                maxHeap.push({first.first - 1, first.second});
            }
            if (second.first > 1) {
                maxHeap.push({second.first - 1, second.second});
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
- Use a max heap to store the frequency of each character to efficiently get the characters with the highest frequency.
- Pop the two characters with the highest frequency from the heap and add them to the result string to ensure no two adjacent characters are the same.
- Push the characters back into the heap with decreased frequency to continue the process until all characters are used.