# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length, t.length <= 10^5`, and `s` and `t` consist of English letters.

## Approach
We will use the sliding window technique to find the minimum window in `s` that contains all characters of `t`. We will maintain two pointers, `left` and `right`, to represent the current window. We will also use an unordered map to store the frequency of characters in `t`.

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
        for (char c : t) tCount[c]++;
        
        int required = tCount.size();
        int left = 0, right = 0;
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int minLength = INT_MAX;
        int minWindow = 0;
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) formed++;
            
            while (left <= right && formed == required) {
                c = s[left];
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    minWindow = left;
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) formed--;
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
Input: s = "aa", t = "aa"
Output: "aa"
```

## Key Takeaways
- Use a sliding window approach to find the minimum window in `s` that contains all characters of `t`.
- Maintain two pointers, `left` and `right`, to represent the current window.
- Use an unordered map to store the frequency of characters in `t` and the current window.