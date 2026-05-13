# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `?` and `*` wildcards. `?` matches any single character, and `*` matches any sequence of characters (including an empty sequence). The function should return `true` if the input string matches the pattern, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", "*")` returns `true`, and `isMatch("cb", "?a")` returns `false`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the matching status of substrings. The algorithm iterates over the input string and pattern, updating the table based on the current characters and wildcards. The final result is stored in the last cell of the table.

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
    
    // Initialize the first row
    for (int j = 1; j <= m; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }
    
    // Fill the table
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
- The `*` wildcard can match any sequence of characters, including an empty sequence.
- The `?` wildcard matches any single character.
- Dynamic programming is used to store the matching status of substrings and avoid redundant computations.