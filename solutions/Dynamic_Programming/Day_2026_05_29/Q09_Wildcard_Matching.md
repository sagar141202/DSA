# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the string matches the pattern, and `false` otherwise. 
For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", "*")` returns `true`, and `isMatch("cb", "?a")` returns `false`.

## Approach
We will use dynamic programming to solve this problem, building a 2D table to track whether each substring of `s` matches each subpattern of `p`. 
The table will be filled in row by row, using the matches of the previous rows to determine the matches of the current row.
The final result will be stored in the last cell of the table.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isMatch(string s, string p) {
    int n = s.size(), m = p.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
    
    // Initialize the base case
    dp[0][0] = true;
    
    // Handle the '*' in the pattern
    for (int j = 1; j <= m; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }
    
    // Fill in the rest of the table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] == '*') {
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            }
        }
    }
    
    return dp[n][m];
}
```

## Test Cases
```
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "*"
Output: true
Input: s = "cb", p = "?a"
Output: false
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- Initialize the base case carefully to ensure the correctness of the solution.
- Handle the '*' character in the pattern separately to ensure correct matching.