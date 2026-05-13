# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The string `s` consists of lowercase English letters. The length of `s` is at most 10000 characters. For example, given `s = "abcabcbb"`, the longest substring without repeating characters is `"abc"`, which has a length of 3. Another example is `s = "bbbbb"`, where the longest substring without repeating characters is `"b"`, which has a length of 1.

## Approach
The approach to solve this problem is to use a sliding window technique with the help of an unordered set to keep track of unique characters in the current substring. We expand the window to the right and when a repeating character is found, we shrink the window from the left until the repeating character is removed.

## Complexity
- Time: O(n)
- Space: O(min(n, m)) where n is the length of the string and m is the size of the character set (in this case, 26 for lowercase English letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize a set to store unique characters in the current substring
        unordered_set<char> charSet;
        
        // Initialize variables to store the maximum length and the current window boundaries
        int left = 0, maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, shrink the window from the left
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
Input: s = "abcabcbb"
Output: 3
Input: s = "bbbbb"
Output: 1
Input: s = "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window technique to efficiently find the longest substring without repeating characters.
- Utilize an unordered set to keep track of unique characters in the current substring.
- The time complexity is linear, making it efficient for large inputs.