# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. For example, given "aab", the output could be "aba". Given "aaab", the output could be an empty string since it is impossible to reorganize the string.

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of each character. We then construct the result string by popping the character with the highest frequency from the queue and appending it to the result string. We also keep track of the previously appended character to ensure that no two adjacent characters are the same.

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

        // Create a priority queue to store characters and their frequencies
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Initialize the result string and a variable to store the previous character
        string result;
        char prev = ' ';

        // Construct the result string by popping characters from the priority queue
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();

            // If the current character is the same as the previous character, 
            // try to append a different character from the priority queue
            if (curr.second == prev && !pq.empty()) {
                auto next = pq.top();
                pq.pop();
                result.push_back(next.second);
                next.first--;
                if (next.first > 0) {
                    pq.push(next);
                }
                prev = next.second;
            } else {
                result.push_back(curr.second);
                curr.first--;
                if (curr.first > 0) {
                    pq.push(curr);
                }
                prev = curr.second;
            }
        }

        // If the length of the result string is equal to the length of the input string, 
        // return the result string; otherwise, return an empty string
        return result.length() == s.length() ? result : "";
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
- Use a priority queue to store characters and their frequencies.
- Keep track of the previously appended character to ensure that no two adjacent characters are the same.
- If it is impossible to reorganize the string, return an empty string.