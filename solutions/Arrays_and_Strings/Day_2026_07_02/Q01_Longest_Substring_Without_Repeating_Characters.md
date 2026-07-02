# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring should be a contiguous sequence of characters within the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b" with a length of 1. The string `s` consists only of English letters and has a length between 0 and 5 * 10^4.

## Approach
We use a sliding window approach with the help of an unordered set to track unique characters in the current window. This allows us to efficiently find the longest substring without repeating characters by expanding and shrinking the window as necessary. The algorithm iterates over the string, adding characters to the set and updating the maximum length found so far.

## Complexity
- Time: O(n)
- Space: O(min(n, m)) where n is the length of the string and m is the size of the character set (in this case, 26 for English letters)

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
- Utilize a sliding window approach to track the current substring without repeating characters.
- Leverage an unordered set for efficient lookup and insertion of characters.
- Keep track of the maximum length of substring without repeating characters found so far.