# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The length of the string is at most 10000 characters. For example, given "abcabcbb", the answer is 3 because the longest substring without repeating characters is "abc". Given "bbbbbb", the answer is 1 because the longest substring without repeating characters is "b". Given "pwwkew", the answer is 3 because the longest substring without repeating characters is "wke".

## Approach
The algorithm uses a sliding window approach with two pointers to track the longest substring without repeating characters. It utilizes an unordered set to store unique characters within the current window. When a repeating character is found, the window is adjusted by moving the left pointer.

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
        // Initialize a set to store unique characters
        unordered_set<char> charSet;
        
        // Initialize variables to store the longest substring length and the current window boundaries
        int left = 0, maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, remove the leftmost character from the set and move the window to the right
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
Input: "bbbbbb"
Output: 1
Input: "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to efficiently track the longest substring without repeating characters.
- Utilize an unordered set to store unique characters within the current window, allowing for constant-time lookups.
- Adjust the window boundaries based on the presence of repeating characters to ensure the substring remains valid.