# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` wildcards. The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element. The function should return `true` if the entire string matches the pattern, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, while `isMatch("aa", "a*")` returns `true`. The input string `s` and pattern `p` only contain characters from the English alphabet and the wildcards `'.'` and `'*'`.

## Approach
The solution uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of the string match the first `j` characters of the pattern. The table is filled in row by row, using the values of previous cells to determine the current cell's value. The function then returns the value of the bottom-right cell, which represents whether the entire string matches the pattern.

## Complexity
- Time: O(len(s) * len(p))
- Space: O(len(s) * len(p))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isMatch(string s, string p) {
    int m = s.size(), n = p.size();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[m][n] = true;
    for (int i = m; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            bool first_match = (i < m && (p[j] == s[i] || p[j] == '.'));
            if (j + 1 < n && p[j + 1] == '*') {
                dp[i][j] = dp[i][j + 2] || (first_match && dp[i + 1][j]);
            } else {
                dp[i][j] = first_match && dp[i + 1][j + 1];
            }
        }
    }
    return dp[0][0];
}
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
- The dynamic programming approach allows for efficient computation of the matching result by avoiding redundant computations.
- The `'*'` wildcard is handled by checking two possibilities: the wildcard matches zero occurrences of the preceding element, or it matches one or more occurrences.
- The function returns the value of the bottom-right cell in the dynamic programming table, which represents whether the entire string matches the pattern.