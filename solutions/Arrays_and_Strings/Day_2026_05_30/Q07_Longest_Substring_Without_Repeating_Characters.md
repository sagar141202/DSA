# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string consists of lowercase English letters. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b" with a length of 1.

## Approach
The solution uses a sliding window approach with two pointers to track the start and end of the current substring. It also utilizes an unordered set to store unique characters within the current substring. The algorithm iterates over the string, expanding the window to the right and adding characters to the set. When a repeating character is found, it shrinks the window from the left until the repeating character is removed from the set.

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
        unordered_set<char> charSet;

        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, shrink the window from the left
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }

            // Add the current character to the set and update the maximum length
            charSet.insert(s[right]);
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
```

## Key Takeaways
- Use a sliding window approach to efficiently track the longest substring without repeating characters.
- Utilize an unordered set to store unique characters within the current substring and handle repeating characters.
- Keep track of the maximum length of the substring without repeating characters.