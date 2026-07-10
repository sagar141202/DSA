# Regular Expression Matching
## Problem Statement
Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*'. The '.' matches any single character, and the '*' matches zero or more of the preceding element. The function should return true if the entire string matches the pattern, and false otherwise. For example, `isMatch("aa", "a")` returns false, `isMatch("aa", ".a")` returns true, and `isMatch("ab", ".*")` returns true.

## Approach
This problem can be solved using dynamic programming, where we build a 2D table to store the match status of substrings and subpatterns. We iterate over the input string and the pattern, updating the table based on the current characters and the preceding elements. The final result is stored in the bottom-right corner of the table.

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
        
        // Initialize the base case
        dp[m][n] = true;
        
        // Fill the last row
        for (int i = n - 1; i >= 0; --i) {
            if (p[i] == '*') {
                dp[m][i] = dp[m][i + 1];
            }
        }
        
        // Fill the rest of the table
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                bool match = s[i] == p[j] || p[j] == '.';
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
Input: s = "aa", p = ".a"
Output: true
Input: s = "ab", p = ".*"
Output: true
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant computations and solve the problem efficiently.
- The 2D table `dp` is used to store the match status of substrings and subpatterns, where `dp[i][j]` represents whether the first `i` characters of `s` match the first `j` characters of `p`.
- The base case is initialized as `dp[m][n] = true`, where `m` and `n` are the lengths of `s` and `p`, respectively.