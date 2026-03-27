# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` special characters. The `'.'` character matches any single character, and the `'*'` character matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. The input string `s` and pattern `p` only contain lowercase letters `a-z`, `'.'`, and `'*'`. The length of `s` is at most 100, and the length of `p` is at most 100.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`. The table is filled in a bottom-up manner, considering the possibilities of matching the current characters in `s` and `p`. The final result is stored in the last cell of the table.

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
- The `'*'` character in the pattern can match zero or more occurrences of the preceding element, which requires special handling in the dynamic programming table.
- The `dp` table is filled in a bottom-up manner to avoid redundant computations and ensure efficient solution.