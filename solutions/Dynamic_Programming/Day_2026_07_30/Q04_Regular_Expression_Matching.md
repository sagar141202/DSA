# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` wildcards. The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, while `isMatch("aa", "a*")` returns `true`.

## Approach
The approach involves using dynamic programming to build a 2D table that tracks whether each substring of `s` matches each substring of `p`. The table is filled in row by row, using the previous rows to determine the current row's values. This allows us to efficiently compute the result for the entire string `s` and pattern `p`.

## Complexity
- Time: O(len(s) * len(p))
- Space: O(len(s) * len(p))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base case where both strings are empty
        dp[m][n] = true;
        
        // Fill in the table for the case where the pattern is empty
        for (int i = m - 1; i >= 0; i--) {
            dp[i][n] = false;
        }
        
        // Fill in the rest of the table
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                bool match = i < m && (p[j] == s[i] || p[j] == '.');
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || match && dp[i + 1][j];
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
Input: s = "aa", p = "a*"
Output: true
Input: s = "ab", p = ".*"
Output: true
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations and improve the efficiency of the solution.
- The 2D table `dp` is used to store the results of subproblems, where `dp[i][j]` represents whether the substring `s[i:]` matches the pattern `p[j:]`.
- The base cases and the recurrence relation are crucial in filling in the table correctly.