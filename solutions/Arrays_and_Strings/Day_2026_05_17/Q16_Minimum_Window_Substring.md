# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window should be a substring of `s` and should contain all characters of `t` with their respective frequencies. For example, if `t = "abc"` and `s = "abcabc"`, the minimum window would be `"abc"`. If `t = "abc"` and `s = "bba"`, the minimum window would be an empty string because there is no substring in `s` that contains all characters of `t`.

## Approach
The algorithm uses a sliding window approach with two pointers, `left` and `right`, to traverse the string `s`. It also uses an unordered map to keep track of the frequency of characters in `t` and another unordered map to keep track of the frequency of characters in the current window.

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
        int ansLeft = 0, ansRight = 0;

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
                    ansLeft = left;
                    ansRight = right;
                }

                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        return ans == INT_MAX ? "" : s.substr(ansLeft, ansRight - ansLeft + 1);
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
- Use a sliding window approach with two pointers to traverse the string `s`.
- Use unordered maps to keep track of the frequency of characters in `t` and the current window.
- Update the minimum window whenever a smaller window is found that contains all characters of `t`.