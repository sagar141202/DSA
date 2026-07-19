# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The length of the string is up to 10000 characters. For example, given "abcabcbb", the answer is 3 because "abc" is the longest substring without repeating characters. Given "bbbbb", the answer is 1 because "b" is the longest substring without repeating characters. Given "pwwkew", the answer is 3 because "wke" is the longest substring without repeating characters.

## Approach
The algorithm uses a sliding window approach with the help of an unordered map to store unique characters in the current window. It expands the window to the right when a new character is found and shrinks it from the left when a repeating character is found. The maximum length of the window is the answer.

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
        // Initialize an unordered map to store unique characters in the current window
        unordered_map<char, int> charIndexMap;
        
        // Initialize variables to store the maximum length and the current window boundaries
        int maxLength = 0, windowStart = 0;
        
        // Iterate over the string
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            // Get the current character
            char rightChar = s[windowEnd];
            
            // If the character is already in the map, update the window start
            if (charIndexMap.find(rightChar) != charIndexMap.end()) {
                windowStart = max(windowStart, charIndexMap[rightChar] + 1);
            }
            
            // Update the character index in the map
            charIndexMap[rightChar] = windowEnd;
            
            // Update the maximum length
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
- Use a sliding window approach to efficiently find the longest substring without repeating characters.
- Utilize an unordered map to store unique characters in the current window and update the window boundaries accordingly.
- Keep track of the maximum length of the window to obtain the final answer.