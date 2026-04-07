# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 500]. For example, given `s = "aab"`, the function should return `"aba"`. However, if `s = "aaab"`, the function should return an empty string because it is impossible to reorganize the string.

## Approach
The approach is to use a priority queue to store the frequency of each character. We then construct the result string by popping the character with the highest frequency from the queue and appending it to the result string. We also keep track of the previously appended character to ensure that no two adjacent characters are the same.

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
        // Count the frequency of each character
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a priority queue to store the frequency of each character
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Initialize the result string and the previously appended character
        string result;
        char prevChar = '\0';

        while (!pq.empty()) {
            // Get the character with the highest frequency
            auto top = pq.top();
            pq.pop();

            // If the previously appended character is the same as the current character,
            // try to append a different character
            if (prevChar == top.second) {
                if (pq.empty()) {
                    // If the queue is empty, it is impossible to reorganize the string
                    return "";
                }
                auto next = pq.top();
                pq.pop();
                result += next.second;
                if (--next.first > 0) {
                    pq.push(next);
                }
                prevChar = next.second;
            }

            // Append the current character to the result string
            result += top.second;
            if (--top.first > 0) {
                pq.push(top);
            }
            prevChar = top.second;
        }

        return result;
    }
};
```

## Test Cases
```
Input: s = "aab"
Output: "aba"
Input: s = "aaab"
Output: ""
```

## Key Takeaways
- Use a priority queue to store the frequency of each character.
- Keep track of the previously appended character to ensure that no two adjacent characters are the same.
- If it is impossible to reorganize the string, return an empty string.