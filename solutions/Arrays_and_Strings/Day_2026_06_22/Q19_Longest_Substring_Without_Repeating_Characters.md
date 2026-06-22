# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The substring must be contiguous and cannot contain any repeating characters. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Given the string "bbbbb", the longest substring without repeating characters is "b" with a length of 1. Given the string "pwwkew", the longest substring without repeating characters is "wke" with a length of 3.

## Approach
Use a sliding window approach to track the longest substring without repeating characters. Utilize an unordered map to store the last seen index of each character. Iterate through the string, updating the map and the window boundaries as necessary. Keep track of the maximum length of the substring seen so far.

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
        unordered_map<char, int> lastSeen;
        int maxLength = 0;
        int windowStart = 0;
        
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            // Update the last seen index of the current character
            if (lastSeen.find(s[windowEnd]) != lastSeen.end()) {
                // Update the window start if the current character has been seen before
                windowStart = max(windowStart, lastSeen[s[windowEnd]] + 1);
            }
            
            // Update the last seen index of the current character
            lastSeen[s[windowEnd]] = windowEnd;
            
            // Update the maximum length of the substring
            maxLength = max(maxLength, windowEnd - windowStart + 1);
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
- Use a sliding window approach to efficiently track the longest substring without repeating characters.
- Utilize an unordered map to store the last seen index of each character, allowing for constant time lookups.
- Update the window boundaries and the maximum length of the substring as necessary to ensure correctness.