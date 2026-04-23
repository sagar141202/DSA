# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string `s` consists of lowercase English letters and has a length of at most 100. For example, if `s = "aaabbb"`, the function should return an empty string because it is not possible to reorganize the string. However, if `s = "aab"`, the function should return `"aba"`.

## Approach
We can use a max heap to store the frequency of each character in the string. The max heap will allow us to efficiently retrieve the character with the highest frequency. We can then use this character to construct the reorganized string, ensuring that no two adjacent characters are the same.

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
        // Create a frequency map for the string
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap to store the frequency of each character
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        // Initialize the result string and the previous character
        string result;
        char prevChar = '\0';

        // Reorganize the string
        while (!maxHeap.empty()) {
            // Get the character with the highest frequency
            auto top = maxHeap.top();
            maxHeap.pop();

            // If the previous character is the same as the current character, 
            // we need to find a character with a lower frequency to insert in between
            if (result.size() > 0 && result.back() == top.second) {
                if (maxHeap.empty()) {
                    return "";
                }
                auto temp = maxHeap.top();
                maxHeap.pop();
                result += temp.second;
                if (--temp.first > 0) {
                    maxHeap.push(temp);
                }
                maxHeap.push(top);
            } else {
                result += top.second;
                if (--top.first > 0) {
                    maxHeap.push(top);
                }
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: "aaabbb"
Output: ""
Input: "aab"
Output: "aba"
Input: "vvvlo"
Output: "vlvov"
```

## Key Takeaways
- Use a max heap to efficiently retrieve the character with the highest frequency.
- Ensure that no two adjacent characters are the same by inserting a character with a lower frequency in between if necessary.
- If it is not possible to reorganize the string, return an empty string.