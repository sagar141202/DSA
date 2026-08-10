# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` wildcards. The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. For example, `isMatch("aa", "a")` returns `false`, while `isMatch("aa", "a*")` returns `true`. The input string `s` and pattern `p` only contain lowercase letters, `'.'`, and `'*'`.

## Approach
The problem can be solved using dynamic programming, where a 2D table is used to store the matching status of substrings. The table is filled in a bottom-up manner, and the final result is stored in the top-right corner of the table. The algorithm iterates over the input string and pattern, and for each character, it checks if the current character in the string matches the current character in the pattern.

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
        dp[m][n] = true;
        
        // Fill the last row of the table
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                bool match = (p[j] == '.' || p[j] == s[i]);
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
- The dynamic programming approach is suitable for this problem, as it allows us to break down the problem into smaller sub-problems and store the results in a table.
- The `'*'` wildcard is handled by checking if the preceding element matches the current character in the string, and if the rest of the string matches the rest of the pattern.
- The `'.'` wildcard is handled by simply checking if the current character in the string matches any character.