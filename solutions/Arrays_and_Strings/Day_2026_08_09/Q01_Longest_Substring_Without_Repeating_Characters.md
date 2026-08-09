# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring must be a contiguous subset of characters in the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b" with a length of 1. The string `s` consists only of English letters and has a length between 0 and 5 * 10^4.

## Approach
We will use a sliding window approach with the help of an unordered set to track unique characters in the current substring. This allows us to efficiently check for repeating characters and update the maximum length of the substring without repeating characters.

## Complexity
- Time: O(n)
- Space: O(min(n, m)), where n is the length of the string and m is the size of the character set (in this case, 26 for English letters)

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
            // While the current character is in the set, remove the leftmost character
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
Input: "bbbbb"
Output: 1
Input: "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to track the current substring without repeating characters.
- Utilize an unordered set to efficiently check for repeating characters in the current substring.
- Update the maximum length of the substring without repeating characters at each step of the sliding window.