# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The length of the string is in the range [0, 5 * 10^4]. For example, given the string "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3. Another example is "bbbbb", the longest substring without repeating characters is "b" with a length of 1.

## Approach
Use a sliding window approach with two pointers to track the substring. Utilize an unordered set to store unique characters within the current window. When a repeating character is found, slide the window to the right of the previous occurrence of the repeating character.

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
        // Initialize variables
        int left = 0; // left pointer of the sliding window
        int maxLength = 0; // maximum length of substring without repeating characters
        unordered_set<char> charSet; // set to store unique characters in the current window

        // Iterate over the string
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
- The sliding window approach is useful for solving substring problems.
- Utilizing an unordered set can efficiently track unique characters within a substring.
- The time complexity of the solution is linear due to the single pass through the string.