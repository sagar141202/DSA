# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it's impossible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 100. For example, given `s = "aab"`, the function should return `"aba"`, and given `s = "aaab"`, the function should return an empty string.

## Approach
The approach is to use a priority queue to store the frequency of each character in the string. We then pop the character with the highest frequency from the queue and append it to the result string. To avoid having two adjacent characters that are the same, we use a temporary variable to store the previous character.

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
        map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a priority queue to store the frequency of each character
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Initialize the result string and a temporary variable
        string res = "";
        pair<int, char> temp;

        // Reorganize the string
        while (!pq.empty()) {
            // Get the character with the highest frequency
            pair<int, char> curr = pq.top();
            pq.pop();

            // If the result string is not empty and the last character is the same as the current character
            if (!res.empty() && res.back() == curr.second) {
                // If the queue is empty, return an empty string
                if (pq.empty()) {
                    return "";
                }

                // Otherwise, get the character with the next highest frequency
                temp = pq.top();
                pq.pop();

                // Append the character to the result string
                res += temp.second;

                // Decrement the frequency of the character
                temp.first--;

                // If the frequency is greater than 0, push the character back into the queue
                if (temp.first > 0) {
                    pq.push(temp);
                }
            }

            // Append the current character to the result string
            res += curr.second;

            // Decrement the frequency of the current character
            curr.first--;

            // If the frequency is greater than 0, push the character back into the queue
            if (curr.first > 0) {
                pq.push(curr);
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
- Reorganize the string by popping the character with the highest frequency from the queue and appending it to the result string.
- Use a temporary variable to store the previous character to avoid having two adjacent characters that are the same.