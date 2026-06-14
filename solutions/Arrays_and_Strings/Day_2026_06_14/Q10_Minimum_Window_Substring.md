# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. For example, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`. If `s = "a"` and `t = "aa"`, return an empty string because there is no window in `s` that contains all characters of `t`.

## Approach
The algorithm uses a sliding window approach to find the minimum window. It maintains a frequency count of characters in `t` and a frequency count of characters in the current window of `s`. The window is expanded to the right until all characters of `t` are included, then it is contracted from the left until a character of `t` is excluded.

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
Input: s = "a", t = "aa"
Output: ""
```

## Key Takeaways
- Use a sliding window approach to expand and contract the window in `s` until the minimum window that contains all characters of `t` is found.
- Maintain frequency counts of characters in `t` and the current window of `s` to efficiently check if all characters of `t` are included in the window.
- Update the minimum window whenever a smaller window that contains all characters of `t` is found.