# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. For example, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`. If `t` is longer than `s`, or if `s` does not contain all characters of `t`, return an empty string.

## Approach
We use a sliding window approach with two pointers to find the minimum window. We also use an unordered map to keep track of the characters in `t` and their frequencies. We then try to match these characters in the current window of `s`.

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
        if (t.size() > s.size()) return "";
        
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
        
        while (right < s.size()) {
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
- Use a sliding window approach to find the minimum window in `s` that contains all characters of `t`.
- Use an unordered map to keep track of the characters in `t` and their frequencies, as well as the characters in the current window of `s`.
- Update the minimum window whenever a smaller window is found that contains all characters of `t`.