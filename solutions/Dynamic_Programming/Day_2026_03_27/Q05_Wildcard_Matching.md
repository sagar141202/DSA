# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules:
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the input string matches the pattern, and `false` otherwise.
For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", "*")` returns `true`, and `isMatch("cb", "?a")` returns `false`.
The input string `s` and pattern `p` only contain lowercase letters, `?`, and `*`.
1 <= `s.length`, `p.length` <= 200

## Approach
The problem can be solved using dynamic programming, where a 2D array `dp` is used to store the matching status of substrings.
The `dp[i][j]` cell represents whether the first `i` characters in `s` match the first `j` characters in `p`.
The final result is stored in `dp[s.length()][p.length()]`.

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
        int m = s.length(), n = p.length();
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
Input: s = "aa", p = "a"
Output: false
Input: s = "aa", p = "*"
Output: true
Input: s = "cb", p = "?a"
Output: false
```

## Key Takeaways
- The `dp` array is used to store the matching status of substrings.
- The `*` character in the pattern can match any sequence of characters, including an empty sequence.
- The `?` character in the pattern can match any single character.