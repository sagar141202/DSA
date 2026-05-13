# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order, and the characters in the window can be repeated. For example, if `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`. The constraints are that `1 <= s.length <= 10^5` and `1 <= t.length <= 10^5`.

## Approach
The approach is to use a sliding window technique with two pointers, `left` and `right`, to traverse the string `s`. We use a hashmap to store the frequency of characters in `t` and another hashmap to store the frequency of characters in the current window. We expand the window to the right and shrink it from the left when the window contains all characters of `t`.

## Complexity
- Time: O(s.length + t.length)
- Space: O(s.length + t.length)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()) return "";
        
        // Create a hashmap to store the frequency of characters in t
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        // Initialize variables
        int left = 0, minLen = INT_MAX, minWindow = "";
        int formed = 0;
        
        // Create a hashmap to store the frequency of characters in the current window
        unordered_map<char, int> windowCounts;
        
        // Traverse the string s
        for (int right = 0; right < s.length(); right++) {
            // Add the character at the right pointer to the window
            char character = s[right];
            windowCounts[character]++;
            
            // If the added character is in t and its frequency in the window is equal to its frequency in t,
            // increment the formed variable
            if (tCount.find(character) != tCount.end() && windowCounts[character] == tCount[character]) {
                formed++;
            }
            
            // While the window contains all characters of t and the left pointer is less than the right pointer,
            // try to shrink the window from the left
            while (left <= right && formed == tCount.size()) {
                character = s[left];
                
                // If the length of the current window is less than the minimum length found so far,
                // update the minimum length and the minimum window
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minWindow = s.substr(left, right - left + 1);
                }
                
                // Remove the character at the left pointer from the window
                windowCounts[character]--;
                
                // If the removed character is in t and its frequency in the window is less than its frequency in t,
                // decrement the formed variable
                if (tCount.find(character) != tCount.end() && windowCounts[character] < tCount[character]) {
                    formed--;
                }
                
                // Move the left pointer to the right
                left++;
            }
        }
        
        return minWindow;
    }
};
```

## Test Cases
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""

Input: s = "aa", t = "aa"
Output: "aa"
```

## Key Takeaways
- Use a sliding window technique with two pointers to traverse the string `s`.
- Use two hashmaps to store the frequency of characters in `t` and the current window.
- Expand the window to the right and shrink it from the left when the window contains all characters of `t`.