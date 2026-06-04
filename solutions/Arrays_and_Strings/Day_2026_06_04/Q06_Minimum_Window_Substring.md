# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order, and the characters in the window can be repeated. For example, if `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`.

## Approach
We use the sliding window technique with two pointers, `left` and `right`, to find the minimum window. We also use a hashmap to store the frequency of characters in `t`. The algorithm expands the window to the right until all characters of `t` are included, then contracts the window from the left until a character of `t` is excluded.

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
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return "";
        }
        
        unordered_map<char, int> tCount;
        for (char c : t) {
            tCount[c]++;
        }
        
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int ans = INT_MAX;
        string ansStr = "";
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            
            while (left <= right && formed == required) {
                c = s[left];
                
                if (right - left + 1 < ans) {
                    ans = right - left + 1;
                    ansStr = s.substr(left, right - left + 1);
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                
                left++;
            }
            
            right++;
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
- The sliding window technique is useful for finding the minimum or maximum window in a string that satisfies certain conditions.
- Using a hashmap to store the frequency of characters can help to efficiently check if all characters of a string are included in a window.
- The `formed` variable is used to keep track of the number of characters in `t` that are formed in the current window.