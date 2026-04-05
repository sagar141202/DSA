# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the input string matches the pattern, and `false` otherwise.
Constraints: `0 <= s.length, p.length <= 2000`
Examples:
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "cb", p = "?a"` Output: `false`
- Input: `s = "adceb", p = "*a*b"` Output: `true`

## Approach
This problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`.
The algorithm fills up the `dp` array in a bottom-up manner, considering the wildcard characters `?` and `*`.
The final result is stored in `dp[s.length()][p.length()]`.

## Complexity
- Time: O(s.length() * p.length())
- Space: O(s.length() * p.length())

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isMatch(string s, string p) {
    int m = s.length(), n = p.length();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    
    // Initialize base cases
    dp[0][0] = true;
    for (int j = 1; j <= n; j++) {
        if (p[j - 1] == '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }
    
    // Fill up the dp array
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
```

## Test Cases
```
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "a*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- The `dp` array is used to store the intermediate results of subproblems.
- The wildcard character `*` can match any sequence of characters, including an empty sequence.
- The function returns `true` if the input string matches the pattern, and `false` otherwise.