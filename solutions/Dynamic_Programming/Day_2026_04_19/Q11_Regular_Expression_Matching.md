# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and '*' matches zero or more of the preceding element. The function should return true if the entire string `s` matches the entire pattern `p`, otherwise return false. For example, `isMatch("aa", "a")` returns false, `isMatch("aa", "a*")` returns true, `isMatch("ab", ".*")` returns true.

## Approach
The approach to solve this problem is to use dynamic programming, where we build a 2D table to store the matching results of substrings and subpatterns. We start by initializing the table and then fill it up based on the matching rules of '.' and '*'. The final result is stored in the bottom-right corner of the table.

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
        
        // Initialize the base case
        dp[m][n] = true;
        
        // Fill up the table
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                bool match = i < m && (p[j] == s[i] || p[j] == '.');
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || match && dp[i + 1][j];
                } else {
                    dp[i][j] = match && dp[i + 1][j + 1];
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
- The dp table is used to store the matching results of substrings and subpatterns.
- The '*' character can match zero or more of the preceding element, so we need to consider two cases: matching zero characters and matching one or more characters.
- The '.' character can match any single character, so we can simply compare the current characters in the string and pattern.