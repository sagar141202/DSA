# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters and has a length between 0 and 10000. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is the string "bbbbb" where the longest substring without repeating characters is "b" with a length of 1.

## Approach
The solution uses a sliding window approach with the help of an unordered set to track unique characters in the current window. The algorithm expands the window to the right and contracts it from the left when a repeating character is found. This ensures that the window always contains unique characters.

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
        // Initialize variables
        int left = 0; // Left pointer of the window
        int maxLength = 0; // Maximum length of substring without repeating characters
        unordered_set<char> charSet; // Set to store unique characters in the window
        
        // Iterate over the string
        for (int right = 0; right < s.length(); right++) {
            // While the character is in the set, remove the leftmost character from the set and move the window to the right
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
- The sliding window approach is useful for problems that require finding a subset of data that meets certain conditions.
- Using an unordered set can significantly reduce the time complexity of the solution by providing constant time complexity for insert and search operations.
- The solution can be optimized further by using a more efficient data structure, such as an unordered map, to store the characters and their indices in the string.