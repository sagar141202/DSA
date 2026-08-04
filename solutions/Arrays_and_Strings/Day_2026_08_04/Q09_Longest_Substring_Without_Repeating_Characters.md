# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The substring must be a contiguous sequence of characters within the string. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc", which has a length of 3. Another example is the string "bbbbb", where the longest substring without repeating characters is "b", which has a length of 1.

## Approach
We will use a sliding window approach to solve this problem, utilizing a set data structure to track unique characters within the current window. The algorithm expands the window to the right, adding characters to the set, and contracts the window from the left when a repeating character is found.

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
        
        // Initialize variables to track the longest substring length and the current window boundaries
        int left = 0, maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.size(); right++) {
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
```

## Key Takeaways
- The sliding window technique is useful for solving problems that involve finding a subset of data that meets certain conditions.
- Using a set data structure can efficiently track unique elements within a window.
- The time complexity of this solution is linear, making it efficient for large inputs.