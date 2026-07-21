# Reorganize String

## Problem Statement
Given a string `s`, reorganize the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 100. For example, given the string "aab", the reorganized string is "aba". However, given the string "aaa", it is impossible to reorganize the string.

## Approach
We can use a max heap to store the frequency of each character in the string. The max heap will allow us to always choose the character with the highest frequency to append to the result string. We will also use a temporary string to store the result.

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

        // Create a max heap to store the frequency of each character
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        // Initialize the result string
        string result;
        while (!maxHeap.empty()) {
            // Get the character with the highest frequency
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();

            // If the result string is not empty and the last character is the same as the current character
            if (!result.empty() && result.back() == first.second) {
                // If the max heap is empty, it is impossible to reorganize the string
                if (maxHeap.empty()) {
                    return "";
                }

                // Get the character with the second highest frequency
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();

                // Append the character with the second highest frequency to the result string
                result += second.second;

                // Decrement the frequency of the character with the second highest frequency
                second.first--;

                // If the frequency of the character with the second highest frequency is greater than 0, push it back to the max heap
                if (second.first > 0) {
                    maxHeap.push(second);
                }

                // Push the character with the highest frequency back to the max heap
                maxHeap.push(first);
            } else {
                // Append the character with the highest frequency to the result string
                result += first.second;

                // Decrement the frequency of the character with the highest frequency
                first.first--;

                // If the frequency of the character with the highest frequency is greater than 0, push it back to the max heap
                if (first.first > 0) {
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
Input: "aaa"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character in the string.
- Always choose the character with the highest frequency to append to the result string.
- Use a temporary string to store the result and handle the case where the last character in the result string is the same as the current character.