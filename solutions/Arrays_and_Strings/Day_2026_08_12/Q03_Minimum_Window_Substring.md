# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length, t.length <= 10^5`, and `s` and `t` consist of English letters.

## Approach
We use a sliding window approach with two pointers, maintaining a frequency count of characters in the window that match characters in `t`. We expand the window to the right until we have all characters of `t`, then contract the window from the left until we no longer have all characters of `t`.

## Complexity
- Time: O(|s| + |t|)
- Space: O(|t|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()) return "";
        
        // Create a hashmap to store the frequency of characters in string t
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;
        unordered_map<char, int> windowCounts;
        int minLength = INT_MAX;
        int minWindow = 0;
        
        // Expand the window to the right
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            
            // If the character is in tCount and its frequency in the window is equal to its frequency in tCount, increment the formed count
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            // Try to contract the window
            while (left <= right && formed == required) {
                c = s[left];
                
                // Update the minimum window
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    minWindow = left;
                }
                
                // Contract the window
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                left++;
            }
            
            right++;
        }
        
        return minLength == INT_MAX ? "" : s.substr(minWindow, minLength);
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
```

## Key Takeaways
- Use a sliding window approach to find the minimum window in `s` that contains all characters of `t`.
- Maintain a frequency count of characters in the window that match characters in `t`.
- Expand the window to the right until we have all characters of `t`, then contract the window from the left until we no longer have all characters of `t`.