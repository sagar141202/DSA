# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters and has a length of at most 10^5. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b" with a length of 1.

## Approach
The approach to solve this problem is to use a sliding window technique along with an unordered set to keep track of unique characters in the current substring. We will maintain two pointers, one at the start and one at the end of the window, and expand the window to the right until we find a repeating character.

## Complexity
- Time: O(n)
- Space: O(min(n, m)) where n is the length of the string and m is the size of the character set (in this case, 128 for ASCII characters)

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
        int maxLength = 0;
        int left = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
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
Input: "bbbbb"
Output: 1
Input: "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to efficiently scan the string and find the longest substring without repeating characters.
- Utilize an unordered set to keep track of unique characters in the current window and ensure O(1) lookup time.
- Be mindful of the character set size (e.g., ASCII, Unicode) when determining the space complexity of the solution.