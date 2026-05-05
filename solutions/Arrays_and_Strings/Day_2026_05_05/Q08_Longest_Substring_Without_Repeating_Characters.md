# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. For example, given "abcabcbb", the answer is 3 because "abc" is the longest substring without repeating characters. Given "bbbbb", the answer is 1 because "b" is the longest substring without repeating characters. Given "pwwkew", the answer is 3 because "wke" is the longest substring without repeating characters.

## Approach
The solution uses a sliding window approach with the help of an unordered set to track unique characters in the current window. We expand the window to the right and shrink it from the left when a repeating character is found.

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
- Utilize an unordered set to efficiently track unique characters in the current window.
- The time complexity is O(n) where n is the length of the string, as each character is visited at most twice.