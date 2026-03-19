# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string consists of English letters, digits, symbols, and spaces. The input string will not be empty, and its length will not exceed 10^5 characters. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc", which has a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b", with a length of 1.

## Approach
The algorithm uses a sliding window approach with the help of an unordered set to track unique characters in the current substring. It iterates over the string, expanding the window to the right when a new character is encountered and shrinking it from the left when a repeating character is found. This approach ensures that the substring within the window always has unique characters.

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
        int maxLength = 0;
        int windowStart = 0;
        // Create an unordered set to store unique characters in the current window
        unordered_set<char> charIndexMap;
        
        // Iterate over the string
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            // Get the current character
            char rightChar = s[windowEnd];
            // Shrink the window from the left if the character is already in the set
            while (charIndexMap.find(rightChar) != charIndexMap.end()) {
                // Remove the leftmost character from the set
                charIndexMap.erase(s[windowStart]);
                // Move the window to the right
                windowStart++;
            }
            // Add the current character to the set
            charIndexMap.insert(rightChar);
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
- Use a sliding window approach to efficiently track the longest substring without repeating characters.
- Utilize an unordered set to store unique characters in the current window, allowing for constant-time lookups and insertions.
- Update the maximum length at each step, ensuring that the longest substring is captured.