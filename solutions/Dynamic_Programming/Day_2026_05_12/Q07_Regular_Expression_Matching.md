# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string matches the pattern, and false otherwise. For example, `isMatch("aa", "a")` returns false, while `isMatch("aa", "a*")` returns true.

## Approach
The solution uses dynamic programming to build a 2D table where each cell represents whether the corresponding substring of `s` matches the corresponding substring of `p`. The algorithm iterates over the input string and pattern, filling in the table based on the current characters and the preceding elements.

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
        for (int i = m; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                // If the current character in the pattern is '*', 
                // then we have two possibilities: 
                // 1. We ignore the '*' and the preceding character, 
                //    so we check if the remaining strings match.
                // 2. We use the '*', so we check if the current character 
                //    in the string matches the preceding character in the pattern,
                //    and then we check if the remaining strings match.
                if (p[j] == '*') {
                    dp[i][j] = dp[i][j + 1] || (i < m && (p[j - 1] == s[i] || p[j - 1] == '.') && dp[i + 1][j]);
                } 
                // If the current character in the pattern is not '*', 
                // then we simply check if the current characters match.
                else {
                    dp[i][j] = i < m && (p[j] == s[i] || p[j] == '.') && dp[i + 1][j + 1];
                }
            }
        }
        
        // The result is stored in the top-left cell of the table
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
- The dynamic programming approach is useful for solving problems with overlapping subproblems.
- The '*' character in the pattern can be handled by considering two possibilities: ignoring the '*' and the preceding character, or using the '*' to match the current character in the string.
- The '.' character in the pattern can be handled by checking if the current character in the string matches any single character.