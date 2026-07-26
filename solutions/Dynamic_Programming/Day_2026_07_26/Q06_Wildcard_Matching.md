# Wildcard Matching
## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules:
- `*` matches any sequence of characters (including an empty sequence).
- `?` matches any single character.
The function should return `true` if the input string matches the pattern, and `false` otherwise.
Constraints: `0 <= s.length, p.length <= 2000`.
Example: Input `s = "aa", p = "a"` should return `false`, while input `s = "aa", p = "a*"` should return `true`.

## Approach
The solution uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`. The final result is stored in the last cell of the table.
The algorithm iterates over the input string and pattern, updating the table based on the current characters and the wildcard rules.

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
                } else if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
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
- The dynamic programming approach allows for efficient computation of the matching result by avoiding redundant calculations.
- The `*` wildcard character can match any sequence of characters, including an empty sequence, which is handled by the `dp[0][j] = dp[0][j - 1]` initialization.
- The `?` wildcard character matches any single character, which is handled by the `dp[i][j] = dp[i - 1][j - 1]` update when `p[j - 1] == '?'`.