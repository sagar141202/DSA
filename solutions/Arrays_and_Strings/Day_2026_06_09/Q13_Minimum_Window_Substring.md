# Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, find the minimum window in `s` that contains all characters of `t`. If there is no such window, return an empty string. The window must contain all characters of `t` in any order, and it should be the smallest possible window. For example, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window is `"BANC"`.

## Approach
The approach involves using a sliding window technique with two pointers, `left` and `right`, to traverse the string `s`. We also use an unordered map to store the frequency of characters in `t` and another map to store the frequency of characters in the current window.

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
Input: s = "aa", t = "aa"
Output: "aa"
```

## Key Takeaways
- The sliding window technique can be used to find the minimum window in a string that contains all characters of another string.
- Using unordered maps to store the frequency of characters can help in efficient lookup and update of character counts.
- The `formed` variable is used to keep track of the number of characters in `t` that are formed in the current window.