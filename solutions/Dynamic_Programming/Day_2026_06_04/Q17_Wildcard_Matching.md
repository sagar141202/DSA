# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for '?' and '*' wildcards. '?' matches any single character, and '*' matches any sequence of characters, including an empty sequence. The function should return true if the string matches the pattern, and false otherwise. For example, "aa" matches "a*" and "aa" matches "?*", but "aaa" does not match "aa".

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents whether the first i characters in the string match the first j characters in the pattern. The '*' wildcard is handled by considering two cases: using the '*' to match zero characters or one or more characters.

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
        
        // Initialize base case: empty string matches empty pattern
        dp[0][0] = true;
        
        // Initialize '*' matching for empty string
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
Input: s = "aa", p = "*"
Output: true
Input: s = "cb", p = "?a"
Output: false
Input: s = "adceb", p = "*a*b"
Output: true
```

## Key Takeaways
- Use dynamic programming to solve string matching problems with wildcards.
- Handle '*' by considering two cases: using the '*' to match zero characters or one or more characters.
- Initialize the base case for empty string and pattern, and then fill the dp table based on the current characters in the string and pattern.