# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` wildcards. The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, while `isMatch("aa", "a*")` returns `true`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the match status of substrings and subpatterns. The table is filled in a bottom-up manner, considering the current character in the string and the current character in the pattern. The `'*'` wildcard is handled by checking the match status of the preceding element.

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
                    dp[i][j] = dp[i][j + 2] || (match && dp[i + 1][j]);
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
- The problem can be solved using dynamic programming with a 2D table.
- The `'*'` wildcard is handled by checking the match status of the preceding element.
- The function returns `true` if the entire string matches the pattern, and `false` otherwise.