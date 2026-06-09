# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. The string can be reorganized if and only if at most one character occurs more than (length of string + 1) / 2 times.

## Approach
We can use a priority queue to store the frequency of each character in the string. The character with the highest frequency is popped from the queue and appended to the result string. We then push the previous character back into the queue if its frequency is greater than 0. This process continues until the queue is empty or the result string is formed.

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
        
        // Initialize the result string
        string res = "";
        
        // Reorganize the string
        while (!pq.empty()) {
            // Get the character with the highest frequency
            pair<int, char> first = pq.top();
            pq.pop();
            
            // If the result string is not empty and the last character is the same as the current character
            if (!res.empty() && res.back() == first.second) {
                // If the queue is empty, it's not possible to reorganize the string
                if (pq.empty()) {
                    return "";
                }
                // Get the character with the next highest frequency
                pair<int, char> second = pq.top();
                pq.pop();
                
                // Append the character with the next highest frequency to the result string
                res += second.second;
                
                // Decrement the frequency of the character
                second.first--;
                
                // If the frequency is greater than 0, push it back into the queue
                if (second.first > 0) {
                    pq.push(second);
                }
                
                // Push the character with the highest frequency back into the queue
                pq.push(first);
            } else {
                // Append the character with the highest frequency to the result string
                res += first.second;
                
                // Decrement the frequency of the character
                first.first--;
                
                // If the frequency is greater than 0, push it back into the queue
                if (first.first > 0) {
                    pq.push(first);
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
- The character with the highest frequency is popped from the queue and appended to the result string.
- If the last character in the result string is the same as the current character, append the character with the next highest frequency to the result string.