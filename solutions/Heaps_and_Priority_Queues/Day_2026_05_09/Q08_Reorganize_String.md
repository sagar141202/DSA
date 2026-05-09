# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. For example, given the string "aaabbbccc", the function should return an empty string because it is not possible to reorganize the string such that no two adjacent characters are the same. However, given the string "aab", the function should return "aba".

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of each character in the string. We then repeatedly pop the two characters with the highest frequency from the queue and append them to the result string. This ensures that no two adjacent characters in the result string are the same.

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

        // Create a priority queue to store the frequency of each character
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }

        // Reorganize the string
        string result;
        while (!pq.empty()) {
            // If the priority queue has only one character left, it is not possible to reorganize the string
            if (pq.size() == 1) {
                if (pq.top().first > 1) {
                    return "";
                } else {
                    result += pq.top().second;
                    pq.pop();
                }
            } else {
                // Pop the two characters with the highest frequency from the queue
                auto first = pq.top();
                pq.pop();
                auto second = pq.top();
                pq.pop();

                // Append the characters to the result string
                result += first.second;
                result += second.second;

                // Decrement the frequency of the characters
                if (first.first > 1) {
                    pq.push({first.first - 1, first.second});
                }
                if (second.first > 1) {
                    pq.push({second.first - 1, second.second});
                }
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
Input: "aaabbbccc"
Output: ""
```

## Key Takeaways
- Use a priority queue to store the frequency of each character in the string.
- Repeatedly pop the two characters with the highest frequency from the queue and append them to the result string.
- If the priority queue has only one character left, it is not possible to reorganize the string if the frequency of the character is greater than 1.