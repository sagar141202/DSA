# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The length of the string is at most 10000 characters. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", the longest substring without repeating characters is "b" with a length of 1.

## Approach
The algorithm uses a sliding window approach with two pointers to track the longest substring without repeating characters. It also uses an unordered set to store unique characters in the current window. The algorithm iterates over the string and expands the window to the right if the character is not in the set, or shrinks the window from the left if the character is in the set.

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
        
        // Initialize two pointers for the sliding window
        int left = 0;
        int maxLength = 0;
        
        // Iterate over the string
        for (int right = 0; right < s.size(); right++) {
            // While the character is in the set, shrink the window from the left
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            
            // Add the character to the set and update the maximum length
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
- Utilize an unordered set to store unique characters in the current window for efficient lookups.
- Update the maximum length of the substring whenever a longer substring is found.