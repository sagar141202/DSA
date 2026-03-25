# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order. The characters in the window can be repeated. For example, if `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`.

## Approach
The approach to solve this problem is to use a sliding window technique with two pointers, `left` and `right`, and a hashmap to keep track of the characters in the window. We expand the window to the right until we have all characters of `t`, then try to shrink the window from the left while still keeping all characters of `t`.

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
        int start = 0, end = 0;

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
- Use a sliding window approach to find the minimum window in `s` that contains all characters of `t`.
- Use a hashmap to keep track of the characters in the window.
- Keep track of the number of characters in `t` that are formed in the window.