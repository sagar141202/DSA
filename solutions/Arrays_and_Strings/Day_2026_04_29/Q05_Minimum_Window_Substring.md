# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are that the length of `s` is at most 100,000 and the length of `t` is at most 100.

## Approach
The algorithm uses a sliding window approach with two pointers, maintaining a frequency count of characters in the window. It expands the window to the right until it contains all characters of `t`, then contracts the window from the left until it no longer contains all characters of `t`.

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
        
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        int required = tCount.size();
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        
        int ans = INT_MAX;
        int start = 0;
        int end = 0;
        
        while (end < s.length()) {
            char c = s[end];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (start <= end && formed == required) {
                c = s[start];
                
                if (end - start + 1 < ans) {
                    ans = end - start + 1;
                    int head = start;
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                start++;
            }
            
            end++;
        }
        
        return ans == INT_MAX ? "" : s.substr(start - (ans - 1), ans);
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
- Use a sliding window approach with two pointers to efficiently scan the string `s`.
- Maintain a frequency count of characters in the window using an unordered map.
- Contract the window from the left when all characters of `t` are found in the window.