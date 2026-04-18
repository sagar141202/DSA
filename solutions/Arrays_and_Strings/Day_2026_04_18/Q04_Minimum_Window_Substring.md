# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If no such window exists, return an empty string. The window must contain all characters of `t` with their respective frequencies. For example, if `t` = "abc", a valid window in `s` must contain at least one 'a', one 'b', and one 'c'. The window should be a substring of `s`.

## Approach
The approach involves using the sliding window technique along with two frequency maps to track the characters in `s` and `t`. We expand the window to the right until all characters of `t` are included, then try to minimize the window by moving the left pointer.

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
        
        unordered_map<char, int> t_count;
        for (char c : t) {
            t_count[c]++;
        }
        
        int required_chars = t_count.size();
        int formed_chars = 0;
        
        unordered_map<char, int> window_counts;
        int left = 0, right = 0;
        int min_len = INT_MAX;
        int min_window = 0;
        
        while (right < s.length()) {
            char c = s[right];
            window_counts[c]++;
            
            if (t_count.find(c) != t_count.end() && window_counts[c] == t_count[c]) {
                formed_chars++;
            }
            
            while (left <= right && formed_chars == required_chars) {
                c = s[left];
                
                if (right - left + 1 < min_len) {
                    min_len = right - left + 1;
                    min_window = left;
                }
                
                window_counts[c]--;
                if (t_count.find(c) != t_count.end() && window_counts[c] < t_count[c]) {
                    formed_chars--;
                }
                
                left++;
            }
            
            right++;
        }
        
        return min_len == INT_MAX ? "" : s.substr(min_window, min_len);
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
- Use two frequency maps to track characters in `s` and `t`.
- Expand the window to the right until all characters of `t` are included, then minimize the window.
- Update the minimum window length and starting index whenever a smaller window is found that contains all characters of `t`.