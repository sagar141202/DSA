# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The string `s` consists of lowercase English letters. The constraints are that the string `s` can have a length of up to 10^5 characters. For example, if `s = "abcabcbb"`, the longest substring without repeating characters is `"abc"` with a length of 3. If `s = "bbbbb"`, the longest substring without repeating characters is `"b"` with a length of 1.

## Approach
The approach to solve this problem is to use a sliding window technique with the help of an unordered set to keep track of unique characters in the current window. We expand the window to the right and when we encounter a repeating character, we shrink the window from the left.

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
        // Initialize a set to store unique characters in the current window
        unordered_set<char> charSet;
        int left = 0; // left pointer of the window
        int maxLength = 0; // maximum length of substring without repeating characters
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, remove the leftmost character from the set and move the left pointer to the right
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
- The use of an unordered set allows for efficient lookup and insertion of characters.
- The sliding window technique enables us to efficiently scan the string and find the longest substring without repeating characters.
- The time complexity of O(n) is achieved by only iterating over the string once.