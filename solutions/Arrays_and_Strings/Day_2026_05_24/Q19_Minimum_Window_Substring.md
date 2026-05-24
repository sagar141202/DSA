# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. For example, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`. If `s = "a"` and `t = "a"`, the minimum window is `"a"`. If `s = "a"` and `t = "aa"`, there is no minimum window, so return an empty string.

## Approach
We use a sliding window approach to find the minimum window. We maintain two pointers, `left` and `right`, to represent the current window. We also use a hashmap to store the frequency of characters in `t`. We expand the window to the right until we have all characters of `t`, then we try to shrink the window from the left.

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
        if (s.empty() || t.empty() || s.size() < t.size()) {
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
Input: s = "a", t = "aa"
Output: ""
```

## Key Takeaways
- Use a sliding window approach to find the minimum window.
- Use a hashmap to store the frequency of characters in `t`.
- Expand the window to the right until we have all characters of `t`, then try to shrink the window from the left.