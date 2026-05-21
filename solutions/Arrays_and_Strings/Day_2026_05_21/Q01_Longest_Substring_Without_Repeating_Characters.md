# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters. The string `s` consists of lowercase English letters. The substring should be a contiguous sequence of characters within `s`. For example, given `s = "abcabcbb"`, the longest substring without repeating characters is `"abc"`, which has a length of 3. Another example is `s = "bbbbb"`, where the longest substring without repeating characters is `"b"`, which has a length of 1.

## Approach
The solution uses a sliding window approach with the help of an unordered set to track unique characters within the current window. The algorithm iterates over the string, expanding the window to the right and adding characters to the set. When a repeating character is found, it slides the window to the right of the previous occurrence of the repeating character.

## Complexity
- Time: O(n)
- Space: O(min(n, m)), where n is the length of the string and m is the size of the character set (in this case, 26 for lowercase English letters)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int left = 0, result = 0;
        
        for (int right = 0; right < s.size(); right++) {
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            charSet.insert(s[right]);
            result = max(result, right - left + 1);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: s = "abcabcbb"
Output: 3
Input: s = "bbbbb"
Output: 1
Input: s = "pwwkew"
Output: 3
```

## Key Takeaways
- Use a sliding window approach to efficiently scan the string and track the longest substring without repeating characters.
- Utilize an unordered set to keep track of unique characters within the current window, allowing for constant time complexity for insertion and lookup operations.
- The solution has a time complexity of O(n), where n is the length of the input string, making it efficient for large inputs.