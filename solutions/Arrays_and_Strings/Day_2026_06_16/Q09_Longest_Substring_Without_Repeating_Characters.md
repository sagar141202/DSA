# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters and has a length of at most 1000 characters. For example, given "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Given "bbbbb", the longest substring without repeating characters is "b" with a length of 1. Given "pwwkew", the longest substring without repeating characters is "wke" with a length of 3.

## Approach
The algorithm uses a sliding window approach with two pointers, start and end, to track the longest substring without repeating characters. It utilizes an unordered set to store unique characters within the current window. The algorithm expands the window to the right by moving the end pointer and shrinks the window from the left by moving the start pointer when a repeating character is found.

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
        unordered_set<char> charSet;
        int left = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.length(); right++) {
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            
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
- Use a sliding window approach to track the longest substring without repeating characters.
- Utilize an unordered set to store unique characters within the current window for efficient lookups.
- Expand and shrink the window based on the presence of repeating characters to find the maximum length.