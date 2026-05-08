# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for '?' and '*' wildcards. The '?' wildcard matches any single character, while the '*' wildcard matches any sequence of characters (including an empty sequence). The function should return `true` if the input string matches the pattern, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, while `isMatch("aa", "*")` returns `true`.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents whether the first `i` characters of the string match the first `j` characters of the pattern. The '*' wildcard is handled by considering two cases: using the '*' to match zero characters or one or more characters.

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
    
    // Initialize base case: empty string matches empty pattern
    dp[0][0] = true;
    
    // Initialize '*' wildcard matches for empty string
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
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve the problem efficiently.
- Handle the '*' wildcard by considering two cases: using it to match zero characters or one or more characters.
- Initialize the base cases carefully to ensure the correctness of the algorithm.