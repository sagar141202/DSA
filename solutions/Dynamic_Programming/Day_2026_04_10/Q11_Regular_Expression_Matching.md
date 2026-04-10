# Regular Expression Matching

## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string matches the pattern, otherwise return false. For example, "aa" matches "a*" and "ab" matches ".*".

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table to track matches between substrings of `s` and `p`. We iterate through both strings, updating the table based on whether the current characters match or if the pattern character is '.' or '*'.

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
        
        // Initialize base case: empty pattern matches empty string
        dp[m][n] = true;
        
        // Fill the last row (empty string) based on the pattern
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                bool match = (s[i] == p[j] || p[j] == '.');
                
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
- Use dynamic programming to solve problems with overlapping subproblems and optimal substructure.
- Initialize the base case carefully, considering all possible scenarios.
- Fill the table in a bottom-up manner, using previously computed values to avoid redundant computation.