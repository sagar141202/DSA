# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` matches any single character
- `*` matches zero or more of the preceding element.
The function should return `true` if the entire string `s` matches the entire pattern `p`, otherwise return `false`.
Examples:
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "ab", p = ".*"` Output: `true`

## Approach
The solution uses dynamic programming to track whether the first `i` characters in `s` match the first `j` characters in `p`.
We build a 2D table `dp` where `dp[i][j]` is `true` if the first `i` characters in `s` match the first `j` characters in `p`.
The final result is stored in `dp[s.size()][p.size()]`.

## Complexity
- Time: O(s.size() * p.size())
- Space: O(s.size() * p.size())

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize base case
        dp[m][n] = true;
        
        // Fill the dp table in a bottom-up manner
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
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The `dp` table is filled in a bottom-up manner to avoid redundant computation.
- The `match` variable is used to check if the current character in `s` matches the current character in `p`.