# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. For example, given "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Given "bbbbb", the longest substring without repeating characters is "b" with a length of 1. Given "pwwkew", the longest substring without repeating characters is "wke" with a length of 3.

## Approach
The algorithm uses a sliding window approach with two pointers, one at the start and one at the end of the current substring, to track the longest substring without repeating characters. It utilizes an unordered set to store unique characters within the current window. When a repeating character is found, the window is slid to the right of the previous occurrence of the repeating character.

## Complexity
- Time: O(n)
- Space: O(min(n, m)) where n is the length of the string and m is the size of the character set

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize variables to store the longest substring length and the current window
        int maxLength = 0;
        int left = 0;
        unordered_set<char> charSet;
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, shrink the window from the left
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            
            // Add the current character to the set and update the max length
            charSet.insert(s[right]);
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
- Utilize a sliding window approach to efficiently track the longest substring without repeating characters.
- Leverage an unordered set for O(1) lookup and insertion of characters within the current window.
- Maintain a variable to store the maximum length of substring without repeating characters encountered so far.