# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for '?' and '*' wildcards. '?' matches any single character, and '*' matches any sequence of characters (including an empty sequence). The function should return true if the input string matches the pattern, and false otherwise. The input string only contains lowercase letters, and the pattern only contains lowercase letters, '?' and '*'. The length of the input string is at most 100, and the length of the pattern is at most 100.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents whether the input string up to a certain index matches the pattern up to a certain index. The table is filled in row by row, using the values from the previous rows to determine the values in the current row. The '*' wildcard is handled by considering two possibilities: using the '*' to match zero characters, or using it to match one or more characters.

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
        
        // handle '*' in the pattern
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // fill in the rest of the table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) {
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
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve the problem efficiently.
- Handle the '*' wildcard by considering two possibilities: using it to match zero characters, or using it to match one or more characters.
- Fill in the table row by row, using the values from the previous rows to determine the values in the current row.