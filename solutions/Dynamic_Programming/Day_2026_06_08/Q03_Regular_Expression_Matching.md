# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string `s` matches the entire pattern `p`, otherwise return false. The input string `s` and pattern `p` only contains characters and '.' and '*'. The length of `s` is less than or equal to 100, and the length of `p` is less than or equal to 100.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the match status of substrings and subpatterns. The table is filled in a bottom-up manner, and the final result is stored in the top-right corner of the table. The algorithm iterates over the input string and pattern, checking for matches between characters and '.' and '*' patterns.

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
        
        // Fill the last row of the table where the string is empty
        for (int i = n - 1; i >= 0; i--) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                // Check if the current characters match or if the pattern is '.'
                bool match = s[i] == p[j] || p[j] == '.';
                
                // If the pattern is '*', check if the '*' matches zero or more of the preceding element
                if (j + 1 < n && p[j + 1] == '*') {
                    dp[i][j] = dp[i][j + 2] || (match && dp[i + 1][j]);
                } else {
                    dp[i][j] = match && dp[i + 1][j + 1];
                }
            }
        }
        
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
- The dynamic programming approach allows for efficient matching of the input string and pattern.
- The 2D table helps to avoid redundant computations and store the match status of substrings and subpatterns.
- The '*' pattern can match zero or more of the preceding element, which requires special handling in the algorithm.