# Longest Substring Without Repeating Characters

## Problem Statement
Given a string, find the length of the longest substring without repeating characters. The string contains only ASCII characters. The length of the string is up to 10000 characters. For example, given "abcabcbb", the answer is 3 because the longest substring without repeating characters is "abc". Given "bbbbb", the answer is 1 because the longest substring without repeating characters is "b". Given "pwwkew", the answer is 3 because the longest substring without repeating characters is "wke".

## Approach
The algorithm uses a sliding window approach with two pointers, start and end, to track the current substring. It also uses an unordered set to store unique characters in the current substring. The algorithm iterates over the string, expanding the window to the right and adding characters to the set. When a repeating character is found, the algorithm shrinks the window from the left until the repeating character is removed from the set.

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
        // Initialize variables
        int start = 0;  // start of the sliding window
        int maxLength = 0;  // maximum length of substring without repeating characters
        unordered_set<char> charSet;  // set to store unique characters in the current substring

        // Iterate over the string
        for (int end = 0; end < s.length(); end++) {
            // While the current character is in the set, shrink the window from the left
            while (charSet.find(s[end]) != charSet.end()) {
                charSet.erase(s[start]);
                start++;
            }

            // Add the current character to the set and update the maximum length
            charSet.insert(s[end]);
            maxLength = max(maxLength, end - start + 1);
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
- Use a sliding window approach to efficiently track the current substring.
- Utilize an unordered set to store unique characters in the current substring and detect repeating characters.
- Update the maximum length of substring without repeating characters at each step.