# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` and the characters in the window can be in any order. The minimum window is defined as the window with the minimum length. If there are multiple minimum windows, return the one with the smallest starting index. For example, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`.

## Approach
The algorithm uses a sliding window approach with two pointers, `left` and `right`, to find the minimum window in `s` that contains all characters of `t`. It maintains a frequency count of characters in `t` and updates the count as the window moves. The window is expanded to the right until all characters of `t` are included, and then it is contracted from the left until a character of `t` is excluded.

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
        int start = 0;
        int end = 0;

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
                    start = left;
                    end = right;
                }

                windowCounts[c]--;
                if (tCount.find(c) != tCount.end() && windowCounts[c] < tCount[c]) {
                    formed--;
                }

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
- Use a sliding window approach with two pointers to find the minimum window in `s` that contains all characters of `t`.
- Maintain a frequency count of characters in `t` and update the count as the window moves.
- The window is expanded to the right until all characters of `t` are included, and then it is contracted from the left until a character of `t` is excluded.