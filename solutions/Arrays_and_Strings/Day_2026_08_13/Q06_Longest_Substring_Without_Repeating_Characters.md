# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The input string will have a length between 0 and 10000 characters. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb", the longest substring without repeating characters is "b" with a length of 1.

## Approach
We use a sliding window approach with two pointers to track the current substring, and a set to store unique characters within the current window. When a repeating character is found, we slide the window to the right by moving the left pointer.

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
        // Initialize a set to store unique characters in the current window
        unordered_set<char> charSet;
        
        // Initialize two pointers for the sliding window
        int left = 0;
        int maxLength = 0;
        
        // Iterate over the string with the right pointer
        for (int right = 0; right < s.length(); right++) {
            // While the current character is in the set, slide the window to the right
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
- Use a sliding window approach to efficiently track the longest substring without repeating characters.
- Utilize a set data structure to store unique characters within the current window, allowing for constant time complexity for lookups and insertions.
- The time complexity is linear, making it efficient for large input strings.