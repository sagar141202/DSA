# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the string matches the pattern, and `false` otherwise. 
For example, `isMatch("aa","a")` returns `false`, `isMatch("aa","*")` returns `true`, and `isMatch("cb","?a")` returns `false`.

## Approach
We use dynamic programming to solve this problem by creating a 2D table to store the matching status of substrings. 
The table is filled based on the rules of wildcard matching. 
The final result is stored in the last cell of the table.

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
        dp[n][m] = true;
        for (int i = n; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                bool match = i < n && (p[j] == s[i] || p[j] == '?');
                if (p[j] == '*') {
                    dp[i][j] = dp[i][j + 1] || (i < n && dp[i + 1][j]);
                } else {
                    dp[i][j] = match && dp[i + 1][j + 1];
                }
            }
        }
        return dp[0][0];
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
- Use dynamic programming to store the matching status of substrings.
- Fill the table based on the rules of wildcard matching.
- The final result is stored in the last cell of the table.