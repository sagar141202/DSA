# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring should be a contiguous sequence of characters within the string. For example, given the string `abcabcbb`, the longest substring without repeating characters is `abc` with a length of 3. If the string is empty, return 0.

## Approach
We will use a sliding window approach with the help of an unordered set to keep track of unique characters in the current window. The algorithm will iterate over the string, expanding the window to the right and shrinking it from the left when a repeating character is found.

## Complexity
- Time: O(n)
- Space: O(min(n, m))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize variables to store the maximum length and the current window
        int maxLen = 0;
        int left = 0;
        unordered_set<char> window;

        // Iterate over the string
        for (int right = 0; right < s.size(); right++) {
            // Shrink the window from the left until the repeating character is removed
            while (window.find(s[right]) != window.end()) {
                window.erase(s[left]);
                left++;
            }

            // Add the current character to the window and update the maximum length
            window.insert(s[right]);
            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
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
Input: ""
Output: 0
```

## Key Takeaways
- Use a sliding window approach to efficiently find the longest substring without repeating characters.
- Utilize an unordered set to keep track of unique characters in the current window.
- The time complexity is O(n) where n is the length of the string, and the space complexity is O(min(n, m)) where m is the size of the character set.