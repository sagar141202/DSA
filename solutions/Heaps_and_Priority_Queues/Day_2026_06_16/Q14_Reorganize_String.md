# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters only. For example, given the string "aab", the function should return "aba". If the string is "aaab", the function should return an empty string.

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of each character. We then pop the two most frequent characters from the queue, append them to the result string, and push them back into the queue with their frequencies decremented. This process continues until the queue is empty or we cannot append a character to the result string without violating the condition.

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
        // Create a frequency map of the characters in the string
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a priority queue to store the characters and their frequencies
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Initialize the result string
        string res;

        // While the priority queue is not empty
        while (!pq.empty()) {
            // Pop the two most frequent characters from the queue
            pair<int, char> p1 = pq.top();
            pq.pop();
            if (pq.empty()) {
                // If the queue only contains one character and its frequency is more than 1, return an empty string
                if (p1.first > 1) {
                    return "";
                } else {
                    // Otherwise, append the character to the result string
                    res += p1.second;
                }
            } else {
                // Pop the second most frequent character from the queue
                pair<int, char> p2 = pq.top();
                pq.pop();

                // Append the two characters to the result string
                res += p1.second;
                res += p2.second;

                // Decrement the frequencies of the two characters
                if (p1.first > 1) {
                    pq.push({p1.first - 1, p1.second});
                }
                if (p2.first > 1) {
                    pq.push({p2.first - 1, p2.second});
                }
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
Input: "aaab"
Output: ""
```

## Key Takeaways
- Use a priority queue to store the frequency of each character in the string.
- Pop the two most frequent characters from the queue, append them to the result string, and push them back into the queue with their frequencies decremented.
- If the queue only contains one character and its frequency is more than 1, return an empty string.