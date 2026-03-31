# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The constraints are: `1 <= s.length, t.length <= 10^5`, and `s` and `t` consist of lowercase English letters.

## Approach
We use a sliding window approach with two pointers, `left` and `right`, to traverse the string `s`. We also maintain a frequency count of characters in `t` and the current window. The algorithm expands the window to the right until it contains all characters of `t`, then contracts the window from the left until it no longer contains all characters of `t`.

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
        int formed = 0;
        
        unordered_map<char, int> windowCounts;
        int left = 0, right = 0;
        int ans = INT_MAX, start = 0, end = 0;
        
        while (right < s.length()) {
            char c = s[right];
            windowCounts[c]++;
            
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) formed++;
            
            while (left <= right && formed == required) {
                c = s[left];
                if (right - left + 1 < ans) {
                    ans = right - left + 1;
                    start = left;
                    end = right;
                }
                
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) formed--;
                left++;
            }
            right++;
        }
        
        return ans == INT_MAX ? "" : s.substr(start, end - start + 1);
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
- Maintain a frequency count of characters in `t` and the current window to track the formation of the window.
- Expand and contract the window based on the formation of the required characters.