# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. '.' matches any single character, and '*' matches zero or more of the preceding element. The function should return true if the entire string `s` matches the entire pattern `p`, otherwise return false. For example, `isMatch("aa", "a")` returns false, `isMatch("aa", "a*")` returns true, and `isMatch("ab", ".*")` returns true.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents whether the substring of `s` matches the substring of `p`. The table is filled in a bottom-up manner, considering the possibilities of '*' and '.'. The final result is stored in the top-right cell of the table.

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
        
        // Fill the last row
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (p[j] == '*') {
                    dp[i][j] = dp[i][j + 1] || (s[i] == p[j - 1] || p[j - 1] == '.') && dp[i + 1][j];
                } else {
                    dp[i][j] = (s[i] == p[j] || p[j] == '.') && dp[i + 1][j + 1];
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
- The '*' character in the pattern can match zero or more occurrences of the preceding character.
- The '.' character in the pattern can match any single character in the input string.
- Dynamic programming is used to efficiently fill the 2D table and avoid redundant computations.