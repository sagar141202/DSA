# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character
- `*` matches any sequence of characters (including an empty sequence)
The function should return `true` if the input string matches the pattern, and `false` otherwise.
Examples: 
- Input: `s = "aa", p = "a"` Output: `false`
- Input: `s = "aa", p = "a*"` Output: `true`
- Input: `s = "cb", p = "?a"` Output: `false`
- Input: `s = "adceb", p = "*a*b"` Output: `true`

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table to track matches between substrings of `s` and `p`.
We iterate through `s` and `p`, updating the table based on whether the current characters match or if we encounter a wildcard.
The final result is stored in the last cell of the table.

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
        int n = s.size(), m = p.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        // Initialize base case: empty pattern matches empty string
        dp[0][0] = true;
        
        // Initialize base case: '*' in pattern can match empty string
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill the dp table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
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
Input: s = "aa", p = "a*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- The `*` wildcard can match any sequence of characters, including an empty sequence.
- The `?` wildcard matches any single character.
- Dynamic programming is used to efficiently compute the matching result by storing intermediate results in a 2D table.