# Wildcard Matching

## Problem Statement
Wildcard Matching is a string matching problem where an unknown character '*' can replace any sequence of characters (including an empty sequence) and '?' can replace any single character. Given two strings, `s` and `p`, determine if `s` matches `p`. The string `s` contains only lowercase letters (a-z), and `p` contains only lowercase letters (a-z) and wildcard characters '*' and '?'. The length of `s` is at most 100 and the length of `p` is at most 200. For example, `s = "aa"` and `p = "a"` should return false, while `s = "aa"` and `p = "*"` should return true.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table to track whether the first `i` characters in `s` match the first `j` characters in `p`. The table is filled in a bottom-up manner, considering all possible matches between characters in `s` and `p`.

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
        int n = s.length(), m = p.length();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        // Initialize the base case
        dp[0][0] = true;
        
        // Fill the first row
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else if (p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = (s[i - 1] == p[j - 1]) && dp[i - 1][j - 1];
                }
            }
        }
        
        return dp[n][m];
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
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve string matching problems with wildcards.
- Initialize the base case carefully and fill the table in a bottom-up manner.
- Consider all possible matches between characters in the input strings.