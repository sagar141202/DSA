# Wildcard Matching

## Problem Statement
Wildcard Matching is a string matching problem where a wildcard pattern, containing '?' and '*', is matched against a given text string. '?' matches any single character, and '*' matches any sequence of characters (including an empty sequence). The goal is to determine whether the wildcard pattern matches the entire text string. The function should return true if the pattern matches the text, and false otherwise. For example, the pattern "a*b" matches the text "aab" but does not match "ab".

## Approach
We use dynamic programming to solve this problem by maintaining a 2D table to track whether the first i characters in the text match the first j characters in the pattern. The table is filled in row by row, with each cell depending on the values of the previous cells. This way, we avoid redundant computation and achieve an efficient solution.

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
                if (p[j - 1] == s[i - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
        
        // The answer is stored in the bottom-right cell
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
- The '*' wildcard can match any sequence of characters, including an empty sequence.
- The '?' wildcard can match any single character.
- Dynamic programming is a powerful technique for solving string matching problems with wildcards.