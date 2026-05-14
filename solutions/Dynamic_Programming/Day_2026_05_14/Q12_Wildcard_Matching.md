# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement a function `isMatch` that checks if `s` matches `p`. The pattern `p` can contain two special characters: `*` (matches any sequence of characters) and `?` (matches any single character). The function should return `true` if `s` matches `p` and `false` otherwise. For example, if `s = "aa"` and `p = "a*"` or `p = "?*"` or `p = "*a"`, the function should return `true`. However, if `s = "aa"` and `p = "?"`, the function should return `false`.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`. The table is filled in row by row, using the values from the previous rows to compute the current row. The final result is stored in the last cell of the table.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        dp[0][0] = true;
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: s = "aa", p = "a*"
Output: true
Input: s = "aa", p = "?*"
Output: true
Input: s = "aa", p = "*a"
Output: true
Input: s = "aa", p = "?"
Output: false
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations and improve the efficiency of the solution.
- The `*` character can match any sequence of characters, including an empty sequence, so we need to handle this case carefully in the dynamic programming table.
- The `?` character can match any single character, so we can simply compare the current characters in `s` and `p` when processing the `?` character.