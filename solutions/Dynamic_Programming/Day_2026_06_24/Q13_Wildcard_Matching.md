# Wildcard Matching
## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `*` matches any sequence of characters (including an empty sequence)
- `?` matches any single character
The function should return `true` if the input string matches the pattern, and `false` otherwise.
Examples: 
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "cb", p = "?a"` Output: `false`
- Input: `s = "adceb", p = "*a*b"` Output: `true`

## Approach
The problem can be solved using dynamic programming, where a 2D array `dp` is used to store the matching status of substrings of `s` and `p`. The algorithm iterates over `s` and `p`, and for each character, it checks if the current character in `p` is `*`, `?`, or a normal character.

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
    dp[0][0] = true;
    for (int j = 1; j <= m; j++) {
        if (p[j - 1] == '*') dp[0][j] = dp[0][j - 1];
    }
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
Input: s = "aa", p = "a*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- The `*` character in the pattern can match any sequence of characters in the input string, including an empty sequence.
- The `?` character in the pattern can match any single character in the input string.
- Dynamic programming is an effective approach to solve this problem, as it avoids redundant computations and improves the efficiency of the solution.