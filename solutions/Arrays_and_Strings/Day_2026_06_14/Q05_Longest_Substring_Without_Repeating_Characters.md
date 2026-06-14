# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring should not contain any repeating characters. For example, given `s = "abcabcbb"`, the longest substring without repeating characters is `"abc"`, which has a length of 3. Another example is `s = "bbbbb"`, where the longest substring without repeating characters is `"b"`, which has a length of 1. The input string `s` will contain only English letters and will have a length between 0 and 5 * 10^4.

## Approach
We use a sliding window approach with two pointers, `left` and `right`, and a set to store unique characters in the current window. We expand the window by moving `right` and add characters to the set. When a repeating character is found, we shrink the window by moving `left` until the repeating character is removed from the set.

## Complexity
- Time: O(n)
- Space: O(min(n, m)), where n is the length of the string and m is the size of the character set (e.g., 128 for ASCII or 256 for extended ASCII)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize the set to store unique characters
        unordered_set<char> charSet;
        
        // Initialize the left pointer and the maximum length
        int left = 0;
        int maxLength = 0;
        
        // Iterate over the string with the right pointer
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, remove the leftmost character
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            
            // Add the current character to the set
            charSet.insert(s[right]);
            
            // Update the maximum length
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
- Use a sliding window approach with two pointers to efficiently scan the string.
- Utilize a set to store unique characters in the current window and detect repeating characters.
- Update the maximum length whenever a longer substring without repeating characters is found.