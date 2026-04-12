# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where: '.' matches any single character, '*' matches zero or more of the preceding element, and the matching should cover the entire string. For example, `isMatch("aa", "a")` returns `false`, `isMatch("aa", "a*")` returns `true`, `isMatch("ab", ".*")` returns `true`.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters in the string match the first `j` characters in the pattern. The solution iterates through the string and pattern, updating the table based on the current characters and the preceding element.

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
- The dynamic programming approach allows for efficient computation of the matching result by avoiding redundant computations.
- The `dp` table is filled in a bottom-up manner to ensure that the values for the preceding elements are available when needed.
- The `match` variable is used to check if the current character in the string matches the current character in the pattern, considering the '.' wildcard.