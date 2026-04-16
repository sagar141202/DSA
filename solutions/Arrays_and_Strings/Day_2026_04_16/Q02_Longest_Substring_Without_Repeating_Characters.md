# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters and has a length of at most 10000 characters. Examples include "abcabcbb" where the longest substring is "abc" with a length of 3, and "bbbbb" where the longest substring is "b" with a length of 1.

## Approach
We use a sliding window approach with two pointers, start and end, to track the substring. We also use an unordered set to store unique characters in the current substring. When a repeating character is found, we move the start pointer forward.

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
        unordered_set<char> charSet;
        int left = 0;
        int maxLength = 0;
        
        for (int right = 0; right < s.size(); right++) {
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
- Use a sliding window approach to efficiently track the longest substring.
- Utilize an unordered set to store unique characters in the current substring.
- Update the maximum length whenever a longer substring without repeating characters is found.