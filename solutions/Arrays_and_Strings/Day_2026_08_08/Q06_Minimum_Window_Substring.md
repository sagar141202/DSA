# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order, and the characters in the window can be repeated. The minimum window is defined as the window with the minimum length. If there are multiple windows with the same minimum length, return the first one. Constraints: `1 <= s.length, t.length <= 10^5`, `s` and `t` consist of lowercase English letters.

## Approach
We use a sliding window approach with two pointers to track the minimum window in `s` that contains all characters of `t`. We maintain a frequency map of characters in `t` and update it as we move the window. The algorithm checks for the presence of all characters of `t` in the current window and updates the minimum window if a smaller window is found.

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
        if (s.length() < t.length()) return "";
        
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        int required = tCount.size();
        int l = 0, r = 0;
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int ans = INT_MAX;
        string ansStr = "";
        
        while (r < s.length()) {
            char c = s[r];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (l <= r && formed == required) {
                c = s[l];
                
                if (r - l + 1 < ans) {
                    ans = r - l + 1;
                    ansStr = s.substr(l, r - l + 1);
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                l++;
            }
            
            r++;
        }
        
        return ansStr;
    }
};
```

## Test Cases
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Input: s = "a", t = "a"
Output: "a"
Input: s = "aa", t = "aa"
Output: "aa"
```

## Key Takeaways
- Use a sliding window approach with two pointers to track the minimum window.
- Maintain a frequency map of characters in `t` and update it as we move the window.
- Check for the presence of all characters of `t` in the current window and update the minimum window if a smaller window is found.