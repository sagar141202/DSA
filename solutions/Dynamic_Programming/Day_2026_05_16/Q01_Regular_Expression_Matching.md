# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` wildcards. The `'.'` wildcard matches any single character, while the `'*'` wildcard matches zero or more of the preceding element. The function should return `true` if the entire string `s` matches the pattern `p`, and `false` otherwise. Constraints: `1 <= s.length <= 20` and `1 <= p.length <= 30`.

## Approach
The solution uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`. The algorithm iterates over the string and pattern, filling in the table based on the current characters and the preceding elements.

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
        
        // Initialize the base case where both string and pattern are empty
        dp[m][n] = true;
        
        // Fill in the table for the case where the pattern is empty
        for (int i = m - 1; i >= 0; --i) {
            dp[i][n] = false;
        }
        
        // Fill in the table for the case where the string is empty
        for (int j = n - 1; j >= 0; --j) {
            if (p[j] == '*') {
                dp[m][j] = dp[m][j + 1];
            } else {
                dp[m][j] = false;
            }
        }
        
        // Fill in the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (p[j] == '*') {
                    // If the current pattern character is '*', consider two cases:
                    // 1. The '*' matches zero characters in the string.
                    // 2. The '*' matches one or more characters in the string.
                    dp[i][j] = dp[i][j + 1] || (dp[i + 1][j] && (p[j - 1] == s[i] || p[j - 1] == '.'));
                } else {
                    // If the current pattern character is not '*', it must match the current string character.
                    dp[i][j] = dp[i + 1][j + 1] && (p[j] == s[i] || p[j] == '.');
                }
            }
        }
        
        // The result is stored in the top-left cell of the table.
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
- The dynamic programming approach allows for efficient computation of the matching result by avoiding redundant calculations.
- The `'*'` wildcard requires special handling, as it can match zero or more of the preceding element.
- The `'.'` wildcard matches any single character, making it a simple case to handle in the algorithm.