# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring should be a contiguous sequence of characters within the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. If the string is "bbbbbb", the longest substring without repeating characters is "b" with a length of 1.

## Approach
We can use a sliding window approach with the help of an unordered set to keep track of unique characters in the current substring. We expand the window to the right if the new character is not in the set, and shrink the window from the left if it is.

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
        // Initialize a set to store unique characters in the current substring
        unordered_set<char> charSet;
        
        // Initialize variables to store the longest substring length and the current window boundaries
        int left = 0, maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.size(); right++) {
            // While the current character is in the set, shrink the window from the left
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            
            // Add the current character to the set and update the maximum length
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
Input: "bbbbbb"
Output: 1
Input: "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to efficiently scan the string and find the longest substring without repeating characters.
- Utilize an unordered set to keep track of unique characters in the current substring, allowing for constant-time lookups and insertions.
- The time complexity is linear due to the single pass through the string, and the space complexity is bounded by the size of the character set or the string length, whichever is smaller.