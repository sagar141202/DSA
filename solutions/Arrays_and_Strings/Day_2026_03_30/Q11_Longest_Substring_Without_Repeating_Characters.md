# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring must be a contiguous sequence of characters within the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Constraints: 0 <= s.length <= 5 * 10^4, s consists of English letters, digits, symbols and spaces.

## Approach
We can use a sliding window approach to track the longest substring without repeating characters. We will maintain a set of unique characters in the current window and update the maximum length as we slide the window to the right. The algorithm will terminate when we have checked all possible substrings.

## Complexity
- Time: O(n)
- Space: O(min(n, m)), where n is the length of the string and m is the size of the character set.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Initialize a set to store unique characters in the current window
        unordered_set<char> charSet;
        
        // Initialize variables to store the maximum length and the current window boundaries
        int left = 0, maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, remove the leftmost character from the set and move the window to the right
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
Input: ""
Output: 0
Input: "abcdefghijklmnopqrstuvwxyz"
Output: 26
```

## Key Takeaways
- Use a sliding window approach to track the longest substring without repeating characters.
- Utilize an unordered set to efficiently store and look up unique characters in the current window.
- Update the maximum length as we slide the window to the right and check all possible substrings.