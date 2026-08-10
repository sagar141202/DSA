# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and has a length of at most 100.

## Approach
Use a max heap to store the frequency of each character. The max heap will help us to always choose the character with the highest frequency. We will then try to append this character to the result string, making sure that no two adjacent characters are the same.

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
        // Create a frequency map
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
            // Get the character with the highest frequency
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            
            // If the result string is not empty and the last character is the same as the current character
            if (!result.empty() && result.back() == first.second) {
                // If the max heap is empty, it's not possible to reorganize the string
                if (maxHeap.empty()) {
                    return "";
                }
                // Get the character with the next highest frequency
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();
                
                // Append the character with the next highest frequency to the result string
                result += second.second;
                // Decrement the frequency of the character
                if (--second.first > 0) {
                    maxHeap.push(second);
                }
                // Push the character with the highest frequency back to the max heap
                maxHeap.push(first);
            } else {
                // Append the character with the highest frequency to the result string
                result += first.second;
                // Decrement the frequency of the character
                if (--first.first > 0) {
                    maxHeap.push(first);
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
Input: "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character.
- Always choose the character with the highest frequency and try to append it to the result string.
- Make sure that no two adjacent characters are the same by checking the last character of the result string.