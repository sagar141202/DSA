# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the input string matches the pattern, and `false` otherwise. 
For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", "*")` returns `true`, and `isMatch("cb", "?a")` returns `false`.

## Approach
The problem can be solved using dynamic programming, where a 2D array `dp` is used to store the matching status of substrings. 
The state `dp[i][j]` represents whether the first `i` characters in `s` match the first `j` characters in `p`.
The transition is based on whether the current character in `p` is `?`, `*`, or a normal character.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        dp[0][0] = true;
        
        // Initialize the first row
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill up the rest of the table
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
- Wildcard matching can be solved using dynamic programming with a 2D array.
- The `*` character can match any sequence of characters, including an empty sequence.
- The `?` character can match any single character.