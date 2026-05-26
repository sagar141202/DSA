# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string consists of lowercase English letters. For example, given "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Given "bbbbb", the longest substring without repeating characters is "b" with a length of 1. Given "pwwkew", the longest substring without repeating characters is "wke" with a length of 3.

## Approach
The algorithm uses a sliding window approach with two pointers, start and end, to track the current substring. It also uses an unordered set to store unique characters in the current substring. When a repeating character is found, the start pointer is moved forward until the repeating character is removed from the set.

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
        // Initialize the set to store unique characters
        unordered_set<char> charSet;
        
        // Initialize the start pointer and the maximum length
        int start = 0, maxLength = 0;
        
        // Iterate over the string with the end pointer
        for (int end = 0; end < s.length(); end++) {
            // While the current character is in the set, remove the character at the start pointer
            while (charSet.find(s[end]) != charSet.end()) {
                charSet.erase(s[start]);
                start++;
            }
            
            // Add the current character to the set
            charSet.insert(s[end]);
            
            // Update the maximum length
            maxLength = max(maxLength, end - start + 1);
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
- Use a sliding window approach to track the current substring
- Use an unordered set to store unique characters in the current substring
- Move the start pointer forward when a repeating character is found to maintain a substring without repeating characters