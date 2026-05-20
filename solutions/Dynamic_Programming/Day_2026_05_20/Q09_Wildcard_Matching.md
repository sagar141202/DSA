# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement wildcard pattern matching with the following rules: 
- `?` matches any single character.
- `*` matches any sequence of characters (including an empty sequence).
The function should return `true` if the string matches the pattern, and `false` otherwise. 
For example, `isMatch("aa","a")` returns `false`, `isMatch("aa","*")` returns `true`, and `isMatch("cb","?a")` returns `false`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the matching status of substrings and subpatterns. 
The table is filled in a bottom-up manner, considering all possible matches of the current character in the string and the pattern. 
The final result is stored in the bottom-right corner of the table.

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
        
        // Return the result
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
- The `*` character in the pattern can match any sequence of characters in the string, including an empty sequence.
- The `?` character in the pattern can match any single character in the string.
- Dynamic programming is used to store the matching status of substrings and subpatterns, reducing the time complexity to O(n*m).