# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring should not contain any repeating characters and all characters are case sensitive. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", the longest substring without repeating characters is "b" with a length of 1.

## Approach
The approach to solve this problem is to use a sliding window technique with the help of an unordered set to store unique characters in the current window. We expand the window to the right and when a repeating character is found, we shrink the window from the left.

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
        // Initialize variables to store the maximum length and the current window
        int maxLength = 0;
        int windowStart = 0;
        
        // Create an unordered set to store unique characters in the current window
        unordered_set<char> charIndexMap;
        
        // Iterate over the string
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            // Get the current character
            char rightChar = s[windowEnd];
            
            // Shrink the window if the character is already in the set
            while (charIndexMap.find(rightChar) != charIndexMap.end()) {
                // Remove the character at the start of the window
                charIndexMap.erase(s[windowStart]);
                // Move the start of the window to the right
                windowStart++;
            }
            
            // Add the current character to the set
            charIndexMap.insert(rightChar);
            
            // Update the maximum length
            maxLength = max(maxLength, windowEnd - windowStart + 1);
        }
        
        // Return the maximum length
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
- Use a sliding window technique to efficiently traverse the string and find the longest substring without repeating characters.
- Utilize an unordered set to store unique characters in the current window and quickly check for repeating characters.
- Update the maximum length whenever a longer substring without repeating characters is found.