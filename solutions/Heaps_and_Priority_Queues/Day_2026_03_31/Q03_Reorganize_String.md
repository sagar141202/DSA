# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and has a length of at most 100. For example, given the string "aab", the reorganized string could be "aba". However, given the string "aaa", it is not possible to reorganize the string, so an empty string should be returned.

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of each character in the string. We then pop the two most frequent characters from the queue, add them to the result string, and push them back into the queue with their frequencies decremented. This process continues until the queue is empty or it is not possible to reorganize the string.

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

        // Create a priority queue to store characters and their frequencies
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Initialize the result string
        string res;
        while (!pq.empty()) {
            // Pop the two most frequent characters from the queue
            pair<int, char> first = pq.top();
            pq.pop();
            if (pq.empty()) {
                // If there is only one character left, it is not possible to reorganize the string
                if (first.first > 1) {
                    return "";
                } else {
                    res += first.second;
                }
                break;
            }
            pair<int, char> second = pq.top();
            pq.pop();

            // Add the characters to the result string
            res += first.second;
            res += second.second;

            // Push the characters back into the queue with their frequencies decremented
            if (first.first > 1) {
                pq.push({first.first - 1, first.second});
            }
            if (second.first > 1) {
                pq.push({second.first - 1, second.second});
            }
        }

        return res;
    }
};
```

## Test Cases
```
Input: "aab"
Output: "aba"
Input: "aaa"
Output: ""
```

## Key Takeaways
- Use a priority queue to store characters and their frequencies.
- Pop the two most frequent characters from the queue and add them to the result string.
- Push the characters back into the queue with their frequencies decremented.