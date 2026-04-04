# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window should contain all characters of `t` with their respective frequencies.

## Approach
We will use a sliding window approach to find the minimum window. We'll maintain two pointers, `left` and `right`, and expand the window to the right until we find all characters of `t`. Then, we'll shrink the window from the left until we no longer have all characters of `t`.

## Complexity
- Time: O(|s| + |t|)
- Space: O(|s| + |t|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty() || s.length() < t.length()) return "";
        
        unordered_map<char, int> tCount;
        for (char c : t) tCount[c]++;
        
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int minLen = INT_MAX;
        int minWindow = 0;
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            if (tCount.count(c) && windowCounts[c] == tCount[c]) formed++;
            
            while (left <= right && formed == required) {
                c = s[left];
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minWindow = left;
                }
                
                windowCounts[c]--;
                if (tCount.count(c) && windowCounts[c] < tCount[c]) formed--;
                left++;
            }
            right++;
        }
        return minLen == INT_MAX ? "" : s.substr(minWindow, minLen);
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
- Use a sliding window approach to find the minimum window.
- Maintain two pointers, `left` and `right`, to expand and shrink the window.
- Use two unordered maps, `tCount` and `windowCounts`, to keep track of the character frequencies in `t` and the current window.