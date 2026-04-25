# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The length of the string is in the range [0, 5 * 10^4]. The string is case sensitive, i.e., 'a' and 'A' are treated as two different characters. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is "bbbbb", where the longest substring without repeating characters is "b" with a length of 1.

## Approach
We will use a sliding window approach with the help of an unordered map to keep track of the characters we have seen so far. The algorithm will iterate over the string and expand the window to the right if the character is not in the map, and shrink the window from the left if the character is already in the map.

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
        // Initialize the map to store characters and their indices
        unordered_map<char, int> charIndexMap;
        
        // Initialize variables to keep track of the maximum length and the current window
        int maxLength = 0;
        int windowStart = 0;
        
        // Iterate over the string
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            // Get the current character
            char rightChar = s[windowEnd];
            
            // If the character is already in the map, shrink the window from the left
            if (charIndexMap.find(rightChar) != charIndexMap.end()) {
                windowStart = max(windowStart, charIndexMap[rightChar] + 1);
            }
            
            // Update the character index in the map
            charIndexMap[rightChar] = windowEnd;
            
            // Update the maximum length
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
- Use a sliding window approach to efficiently find the longest substring without repeating characters.
- Utilize an unordered map to keep track of characters and their indices, allowing for constant time lookups and updates.
- Be mindful of the window boundaries and update them accordingly to ensure the correct substring is considered.