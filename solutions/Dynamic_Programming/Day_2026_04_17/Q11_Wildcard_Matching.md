# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for '?' and '*' wildcards. '?' matches any single character, and '*' matches any sequence of characters (including an empty sequence). The function should return true if the string matches the pattern, and false otherwise. The input string `s` and pattern `p` only contain lowercase English letters, '?' and '*'. 1 <= s.length, p.length <= 200.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents whether the first i characters in the string match the first j characters in the pattern. We iterate over the string and pattern, updating the table based on the current characters and the '*' and '?' wildcards.

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
        
        // Initialize the base case where the pattern is empty
        dp[0][0] = true;
        
        // Initialize the base case where the string is empty
        for (int j = 1; j <= m; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill in the rest of the table
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
- The '*' wildcard can match any sequence of characters, including an empty sequence.
- The '?' wildcard can match any single character.
- Dynamic programming is used to efficiently build the 2D table and avoid redundant computations.