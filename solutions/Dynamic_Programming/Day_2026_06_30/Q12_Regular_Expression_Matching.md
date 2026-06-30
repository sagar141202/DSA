# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` wildcards. The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, while `isMatch("aa", "a*")` returns `true`.

## Approach
This problem can be solved using dynamic programming, where a 2D table is used to store the matching status of substrings and subpatterns. The algorithm iterates over the input string and pattern, filling the table based on the matching rules for `'.'` and `'*'`. The final result is stored in the bottom-right corner of the table.

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
        
        // Initialize the base case
        dp[m][n] = true;
        
        // Fill the table in a bottom-up manner
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
- The dynamic programming approach is suitable for solving problems with overlapping subproblems, such as regular expression matching.
- The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element.
- The 2D table `dp` is used to store the matching status of substrings and subpatterns, where `dp[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`.