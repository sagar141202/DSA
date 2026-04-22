# Wildcard Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement a function `isMatch` that returns `true` if `s` matches `p`, and `false` otherwise. The pattern `p` may contain two special characters: `?` (which can match any single character) and `*` (which can match any sequence of characters, including an empty sequence). The function should return `true` if there exists a match, and `false` otherwise. For example, `isMatch("aa","a")` returns `false`, `isMatch("aa","*")` returns `true`, and `isMatch("cb","?a")` returns `false`.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`. The function iterates through the input string and pattern, updating the table based on the current characters and the values in the previous cells. The final result is stored in the last cell of the table.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base case: an empty string matches an empty pattern
        dp[0][0] = true;
        
        // Initialize the base case: an empty string matches a pattern that starts with '*'
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
        
        // Fill in the rest of the table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current characters match or the pattern character is '?', update the table
                if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                // If the pattern character is '*', update the table based on the previous characters
                else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
        
        // Return the result stored in the last cell of the table
        return dp[m][n];
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
- Dynamic programming is a suitable approach for solving problems that have overlapping subproblems, such as the wildcard matching problem.
- The table should be initialized carefully to handle the base cases, such as an empty string matching an empty pattern or a pattern that starts with '*'.
- The function should update the table based on the current characters and the values in the previous cells, considering the special characters '?' and '*'.