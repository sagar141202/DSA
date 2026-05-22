# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. For example, given `s = "aab"`, the output should be `"aba"`. However, if `s = "aaab"`, the output should be an empty string because it is impossible to reorganize the string such that no two adjacent characters are the same.

## Approach
The algorithm uses a max heap to store the frequency of each character. It pops the two most frequent characters from the heap, adds them to the result string, and then pushes them back into the heap with decremented frequencies. This process continues until the heap is empty or it is impossible to reorganize the string.

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

        // Create a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        string result;
        while (!maxHeap.empty()) {
            // Pop the two most frequent characters from the heap
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (maxHeap.empty()) {
                // If the heap only contains one character, it is impossible to reorganize the string
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

            // Push the characters back into the heap with decremented frequencies
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
- Use a max heap to store the frequency of each character.
- Pop the two most frequent characters from the heap, add them to the result string, and then push them back into the heap with decremented frequencies.
- If the heap only contains one character and its frequency is greater than 1, it is impossible to reorganize the string.