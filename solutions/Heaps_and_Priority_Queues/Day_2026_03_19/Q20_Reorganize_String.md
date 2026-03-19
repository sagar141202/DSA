# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is at most 100. For example, given the string "aab", the reorganized string would be "aba". However, given the string "aaab", it is not possible to reorganize the string.

## Approach
We will use a max heap to store the frequency of each character in the string. We will then pop the two most frequent characters from the heap, append them to the result string, and push them back into the heap with their frequencies decremented. This process will continue until the heap is empty or we are not able to append a character to the result string without violating the condition.

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
        // Create a frequency map of characters
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap to store the frequency of characters
        priority_queue<pair<int, char>> maxHeap;
        for (auto &it : freq) {
            maxHeap.push({it.second, it.first});
        }

        // Initialize the result string
        string result;

        // Reorganize the string
        while (!maxHeap.empty()) {
            // Pop the two most frequent characters from the heap
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (maxHeap.empty()) {
                // If there is only one character left and the last character in the result string is the same, return an empty string
                if (result.size() > 0 && result.back() == first.second) {
                    return "";
                }
                result += first.second;
                break;
            }
            pair<int, char> second = maxHeap.top();
            maxHeap.pop();

            // Append the two characters to the result string
            result += first.second;
            result += second.second;

            // Push the two characters back into the heap with their frequencies decremented
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
- Use a max heap to store the frequency of each character in the string.
- Pop the two most frequent characters from the heap, append them to the result string, and push them back into the heap with their frequencies decremented.
- If there is only one character left and the last character in the result string is the same, return an empty string.