# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it's impossible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 100. For example, given `s = "aab"`, the output should be `"aba"`. However, given `s = "aaab"`, the output should be an empty string because it's impossible to reorganize the string.

## Approach
The algorithm uses a priority queue to store characters and their frequencies. It pops the two most frequent characters from the queue, adds them to the result string, and then pushes them back into the queue if their frequencies are greater than 0. This process continues until the queue is empty or it's impossible to reorganize the string.

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
        map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a priority queue
        priority_queue<pair<int, char>> pq;
        for (auto& p : freq) {
            pq.push({p.second, p.first});
        }

        // Initialize result string and previous character
        string result;
        pair<int, char> prev = {0, '#'};

        while (!pq.empty()) {
            // Get the most frequent character
            pair<int, char> cur = pq.top();
            pq.pop();

            // If the current character is the same as the previous one, return an empty string
            if (prev.first > 0 && cur.second == prev.second) {
                return "";
            }

            // Add the current character to the result string
            result += cur.second;

            // Decrease the frequency of the current character
            cur.first--;

            // Push the previous character back into the queue if its frequency is greater than 0
            if (prev.first > 0) {
                pq.push(prev);
            }

            // Update the previous character
            prev = cur;
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
- Use a priority queue to store characters and their frequencies.
- Always try to add the most frequent character to the result string.
- If the current character is the same as the previous one, return an empty string because it's impossible to reorganize the string.