# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where: '.' matches any single character, '*' matches zero or more of the preceding element, and the matching should cover the entire string. For example, if `s = "aa"` and `p = "a"`, the function should return `false`; if `s = "aa"` and `p = "a*"` or `p = ".*"`, the function should return `true`. The input strings and patterns are non-empty and only contain characters `a-z`, `.`, and `*`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table where each cell represents whether the substring of `s` matches the substring of `p`. We fill up this table by comparing characters from `s` and `p` and using the properties of `.` and `*`.

## Complexity
- Time: O(len(s) * len(p))
- Space: O(len(s) * len(p))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base case: empty pattern matches empty string
        dp[m][n] = true;
        
        // Fill up the last row where the pattern can still match the empty string
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill up the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                // If the current characters match or the pattern is '.', consider the next characters
                if (p[j] == '.' || p[j] == s[i]) {
                    dp[i][j] = dp[i + 1][j + 1];
                } 
                // If the pattern is followed by '*', consider two cases: using '*' or not using '*'
                else if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || (p[j] == '.' || p[j] == s[i]) && dp[i + 1][j];
                }
            }
        }
        
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: s = "aa", p = "a"
Output: false

Input: s = "aa", p = "a*"
Output: true

Input: s = "ab", p = ".*"
Output: true
```

## Key Takeaways
- The dynamic programming approach allows us to break down the problem into smaller sub-problems and store their solutions to avoid redundant computation.
- The properties of `.` and `*` are crucial in determining whether a substring of `s` matches a substring of `p`.
- The base case where the pattern is empty is a key part of initializing the dynamic programming table.