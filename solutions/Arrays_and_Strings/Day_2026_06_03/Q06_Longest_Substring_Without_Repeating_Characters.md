# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The input string will only contain ASCII characters, and the length of the string will not exceed 1000. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Given the string "bbbbb", the longest substring without repeating characters is "b" with a length of 1. Given the string "pwwkew", the longest substring without repeating characters is "wke" with a length of 3.

## Approach
We will use a sliding window approach with the help of an unordered set to store unique characters in the current window. The algorithm will iterate over the string and expand the window to the right if the character is not in the set, and shrink the window from the left if the character is in the set.

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
        unordered_set<char> set;
        int left = 0, result = 0;
        for (int right = 0; right < s.length(); right++) {
            // shrink the window if the character is in the set
            while (set.find(s[right]) != set.end()) {
                set.erase(s[left]);
                left++;
            }
            // expand the window
            set.insert(s[right]);
            result = max(result, right - left + 1);
        }
        return result;
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
- The sliding window approach is useful for solving problems that involve finding a subset of data that meets certain conditions.
- Using an unordered set to store unique characters can help reduce the time complexity of the solution.
- The time complexity of the solution is O(n) because each character in the string is visited at most twice (once by the right pointer and once by the left pointer).