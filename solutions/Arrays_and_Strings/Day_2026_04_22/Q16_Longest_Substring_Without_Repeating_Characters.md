# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring must be a contiguous sequence of characters within the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Similarly, for the string "bbbbb", the longest substring without repeating characters is "b" with a length of 1. The string `s` consists only of English letters and has a length between 0 and 5 * 10^4.

## Approach
The solution utilizes a sliding window approach with the help of an unordered map to track unique characters within the current window. This allows for efficient identification of repeating characters and adjustment of the window boundaries. The algorithm iterates through the string, expanding the window to the right when a new character is encountered and contracting it from the left when a repeating character is found.

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
        unordered_map<char, int> charIndexMap;
        int maxLength = 0;
        int windowStart = 0;
        
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char rightChar = s[windowEnd];
            if (charIndexMap.find(rightChar) != charIndexMap.end()) {
                windowStart = max(windowStart, charIndexMap[rightChar] + 1);
            }
            
            charIndexMap[rightChar] = windowEnd;
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
- Utilize a sliding window approach to efficiently scan the string and identify the longest substring without repeating characters.
- Leverage an unordered map to track the index of each character, enabling quick detection of repeating characters and adjustment of the window boundaries.
- Maintain a variable to store the maximum length of substring without repeating characters encountered so far.