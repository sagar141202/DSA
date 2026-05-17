# Longest Substring Without Repeating Characters

## Problem Statement
Given a string s, find the length of the longest substring without repeating characters. The string may contain any ASCII characters. For example, if the input string is "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. If the input string is "bbbbb", the longest substring without repeating characters is "b" with a length of 1. The constraints are 0 <= s.length <= 5 * 10^4 and the string only contains ASCII characters.

## Approach
The algorithm uses a sliding window approach with the help of an unordered map to store the last seen index of each character. It iterates over the string, expanding the window to the right and contracting it from the left when a repeating character is found. The maximum length of the substring without repeating characters is updated at each step.

## Complexity
- Time: O(n)
- Space: O(min(n, m)), where n is the length of the string and m is the size of the character set (256 for ASCII)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize variables
        int left = 0; // left pointer of the sliding window
        int maxLength = 0; // maximum length of substring without repeating characters
        unordered_map<char, int> charIndexMap; // map to store the last seen index of each character

        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // If the character is already in the map and its index is within the current window
            if (charIndexMap.find(s[right]) != charIndexMap.end() && charIndexMap[s[right]] >= left) {
                // Move the left pointer to the right of the repeating character
                left = charIndexMap[s[right]] + 1;
            }

            // Update the last seen index of the character
            charIndexMap[s[right]] = right;

            // Update the maximum length of substring without repeating characters
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};
```

## Test Cases
```
Input: "abcabcbb"
Output: 3
Input: "bbbbb"
Output: 1
Input: "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to efficiently iterate over the string and find the longest substring without repeating characters.
- Utilize an unordered map to store the last seen index of each character and contract the window when a repeating character is found.
- Update the maximum length of substring without repeating characters at each step to ensure the correct result.