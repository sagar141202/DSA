# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The function should return the minimum window substring of `s` that contains all characters of `t`. If there are multiple such windows, return the first one. Constraints: `1 <= s.length, t.length <= 10^5`, `s` and `t` consist of lowercase English letters.

## Approach
We use a sliding window approach with two pointers to track the minimum window in `s` that contains all characters of `t`. We maintain a frequency count of characters in `t` and update it as we slide the window. The algorithm expands the window to the right until all characters of `t` are found, then contracts the window from the left until a character of `t` is no longer present.

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
        string res = "";
        
        while (end < s.length()) {
            char c = s[end];
            windowCounts[c]++;
            if (tCount.find(c) != tCount.end() && windowCounts[c] == tCount[c]) {
                formed++;
            }
            while (formed == required && start <= end) {
                if (end - start + 1 < ans) {
                    ans = end - start + 1;
                    res = s.substr(start, end - start + 1);
                }
                char c = s[start];
                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }
                start++;
            }
            end++;
        }
        return res;
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
- Use a sliding window approach to track the minimum window that contains all characters of `t`.
- Maintain frequency counts of characters in `t` and the current window to efficiently update the window boundaries.
- The algorithm has a linear time complexity due to the single pass through the string `s`.